import ast
import json
import os
import atexit
import sys
from proglib.var2json import *


class unuse:
    pass


class file_writer:
    def __init__(self, path):
        self.path = path
        if not os.path.exists(path):
            open(path, "w")
        self.text = open(path, "r+", encoding="utf-8").read()

    def write(self, text):
        self.text = text
        with open(self.path, "w", encoding="utf-8") as f:
            f.write(text)


class LRUcache:  # 双向链表LRU 缓存
    def __init__(self, size=8):
        self.data = []
        self.size = size

    def __str__(self):
        return f"LRUcache:(size={self.size}, data={self.data})"

    def __repr__(self):
        return self.__str__()

    def pop(self):  # 获取
        self.data.pop()

    def push(self, item):  # 添加
        self.data.append(item)
        if len(self.data) > self.size:
            self.data.pop(0)


class NBText:  # 文本类
    def __init__(self, text=None, path=("", ""), size=16):
        self.root, self.path = path  # 文件路径
        self.path = os.path.join(self.root, self.path)
        if not os.path.exists(self.root):
            os.makedirs(self.root)
        self.file = file_writer(self.path)  # 文件写入器
        if text is not None:
            self.text = text
        else:
            self.text = self.file.text
        self.history = LRUcache(size)  # 历史记录
        self.history.push(self.text)

    def __str__(self):
        return f"NBText:(path={self.path}, text={self.text})"

    def __repr__(self):
        return self.__str__()

    def cancel(self):
        return self.history.pop()

    def input(self, text):
        self.text = text
        self.history.push(self.text)

    def save(self, path=None):  # 保存
        if path is None:
            self.file.write(self.text)
        else:
            open(path, "w", encoding="utf-8").write(self.text)


class NBVar:  # 变量类
    def __init__(self, name, value, vtype=None):
        self.name = name  # 变量名
        # 自动处理
        self.eval = eval
        self.safe_eval = ast.literal_eval
        if vtype is None:
            self.type = self.eval
            try:
                self.value = self.eval(value, {})
            except:
                self.value = value
        self.type = vtype  # 类型

    def __str__(self):
        return f"NBVar:(name={self.name}, value={self.value}, type={(type(self.type) if self.type!=self.eval and self.type!=self.safe_eval else 'auto')})"

    def __repr__(self):
        return self.__str__()

    def input(self, value, vtype=None):
        if vtype is None:
            self.type = self.safe_eval
            try:
                self.value = self.safe_eval(value)
            except:
                self.value = value
        self.type = vtype  # 类型


class NBVarGroup:  # 变量组类
    def __init__(self, vars=None, path=("", ""), j2o={}):
        self.root, self.path = path
        self.path = os.path.join(self.root, self.path)
        self.j2o = j2o
        if vars is not None:
            self.vars = vars
        else:
            self.vars = {}
            if self.path != "":
                self.load_json(self.path, self.j2o)

    def __str__(self):
        return f"NBVar_Group:(path={self.path}, var_group={self.vars})"

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, name):
        return self.vars[name]

    def __setitem__(self, name, **input):
        self.vars[name].input(**input)

    def __delitem__(self, name):
        self.vars.pop(name)

    def load_json(self, path, j2o={}):  # 加载
        file = json.load(open(path, encoding="utf-8"),  # JSON文件字典
                         object_hook=NBJsonDecoder(j2o))
        self.load_dict(file)

    def load_dict(self, dic):  # 加载
        for v in dic:
            self.vars[v] = NBVar(v, dic[v])

    def dict_output(self):  # 保存
        return {v.name: v.value for v in list(self.vars.values())}  # JSON文件字典

    def add(self, **kwarg):
        self.vars[kwarg["name"]] = NBVar(**kwarg)


class NBPlugin:  # 插件类
    def __init__(self, pclass, info: dict = {}, path=None):
        self.pclass = pclass
        self.main = self.pclass.main if "main" in dir(
            self.pclass) else lambda: None
        self.quit = self.pclass.quit if "quit" in dir(
            self.pclass) else lambda: None
        self.info = info
        self._path = path

    def __str__(self):
        return f"NBPlugin:(plugin={self.pclass}, info={self.info},hash=)"

    def __repr__(self):
        return self.__str__()


note_config_file = "note.json"


class NoteBook:  # 程序核心类
    def __init__(self):
        self.text = {}  # 文本
        self.var_group = {}  # 变量组
        self.save = [None, None]  # 保存
        self.plugins = {}  # 查检字典
        self.lib = {}  # 支持库
        self.inuse = None  # 运行插件
        self.obj2json = {}  # 变量转JSON
        self.json2obj = {}  # JSON转变量

    def __str__(self):
        return f"NoteBook(text={self.text}, var_group={self.var_group}, plugins={self.plugins})"

    def __repr__(self):
        return self.__str__()

    def _save2file(self, path):  # 保存到文件
        pass

    def _save2dir(self, path):  # 保存到目录
        if not os.path.exists(path):  # 创建目录
            os.makedirs(path)
        json_file = {  # JSON文件字典, 文件路径
            "text": {n: os.path.relpath(self.text[n].path, self.text[n].root) for n in self.text},
            "var": {v: os.path.relpath(self.var_group[v].path, self.var_group[v].root) for v in self.var_group}
        }
        json.dump(json_file, open(os.path.join(path, note_config_file),  # 写入
                  "w"), ensure_ascii=False, indent=4)
        for t in list(self.text.values()):  # 保存文本
            t.save(os.path.join(path, os.path.relpath(t.path, t.root)))
        for v in zip([n.dict_output() for n in list(self.var_group.values())], [os.path.relpath(v.path, v.root) for v in list(self.var_group.values())]):  # 保存变量组
            json.dump(v[0], open(os.path.join(path, v[1]),
                                 "w"), default=NBJsonEncoder(self.obj2json), ensure_ascii=False, indent=4)

    def output_save(self, path=None, type=None):
        if path is None:
            spath = self.save[0]
        else:
            spath = path
        if type is None:
            stype = self.save[1]
        else:
            stype = type
        if stype == "dir":  # 保存方式为目录时
            self.save[1] = "dir"
            self._save2dir(spath)
        elif stype == "file":  # 保存方式为文件时
            self.save[1] = "file"
            self._save2file(spath)

    def _file2note(self, path):  # 加载文件到程序
        c = json.load(open(path, encoding="utf-8"))
        if "text" in c:  # 加载文本
            for t in c["text"]:
                self.text[t] = NBText(text=c["text"][t])
        else:
            self.text = {}
        if "var" in c:  # 加载变量
            for v in c["var"]:
                self.var_group[v] = NBVarGroup(value=c["var"][v])
        else:
            self.var_group = {}

    def _dir2note(self, path):  # 加载目录到程序
        try:
            c = json.load(
                open(os.path.join(path, note_config_file), encoding="utf-8"))
        except Exception as e:
            raise e
        self.text = {}
        self.var_group = {}
        if "text" in c:  # 加载文本
            for t in c["text"]:
                self.text[t] = NBText(path=(path, c["text"][t]))
        if "var" in c:  # 加载变量
            for v in c["var"]:
                self.var_group[v] = NBVarGroup(
                    path=(path, c["var"][v]), j2o=self.json2obj)

    def note_set(self, path):  # 加载笔记
        if os.path.isfile(path):
            self.save = [path, "file"]
            self._file2note(path)
        if os.path.isdir(path):
            self.save = [path, "dir"]
            self._dir2note(path)

    def save_set(self, path):  # 保存设置
        if path == "":  # 不保存
            self.save = None
            try:
                atexit.unregister(self.output_save)  # 取消自动保存
            except:
                pass
        atexit.register(self.output_save)  # 开启自动保存

    def text_add(self, name, **kwargs):  # 添加文本
        self.text[name] = NBText(**kwargs)

    def var_group_add(self, name, **kwargs):  # 添加变量
        self.var_group[name] = NBVarGroup(**kwargs)

    def plugin_quit(self):  # 退出当前运行插件
        self.inuse.quit() if self.inuse is not None else None

    def plugin_back_func(self, p):  # 基于输入的插件类返回一个执行插件的函数
        def back():
            if self.inuse != None:  # 退出运行插件
                self.plugin_quit()
            if self.inuse == p:  # 退出插件
                return None
            self.inuse = p
            p.main()

        return back

    def plugin_back_name(self, name):  # 基于输入的插件名称返回一个执行插件的函数
        return self.plugin_back_func(self.plugins[name][0])

    def _add_lib(self, path, key=None):  # 加载支持库
        scope = {"sys": sys, "os": os}
        name = os.path.basename(path).split('.')[0]
        if key is None:
            key = name
        # 加载代码
        lc = f"sys.path.append('{os.path.dirname(path)}');import {name}"
        exec(lc, scope)
        lib = scope[name]
        lib._path = path
        self.lib[key] = lib

    def _add_plugin(self, path, name=None, run=None):
        if run is None:
            run = self
        scope = {"sys": sys, "os": os}  # 设置作用域
        file = os.path.basename(path).split('.')[0]
        # 加载代码
        lc = f"sys.path.append('{os.path.dirname(path)}');import {file};p={file}.{name+'Run'}"
        exec(lc, scope)  # 初始化插件
        scope.pop('__builtins__')
        if name == None:  # 设置插件名称
            name = scope["name"]
        plugin_l = {}
        try:
            p = scope["p"](run)
        except Exception as e:
            raise RuntimeError(
                f"Plugin({path}):{e}")
        if "__other__" in scope:  # 添加其他信息
            for a in scope["__other__"]:
                plugin_l[a] = scope[a]
        self.plugins[name] = NBPlugin(
            p, plugin_l, path=path)

    def plugin_list(self, path):  # 获取文件夹内所有插件
        ld = os.listdir(path)
        if "plugin.json" in ld:  # 当文件夹含有插件时
            t = json.load(
                open(os.path.join(path, "plugin.json"), encoding="utf-8"))
            if "unuse" in t:
                if t["unuse"] == True:
                    return [None]
            if "type" in t:
                if t["type"] == "lib":  # 插件类型为库时
                    t = 0
                elif t["type"] == "plugin":  # 插件类型为功能型插件时
                    t = t["rank"] if "rank" in t else 1
                else:
                    t = 1
            else:
                t = 1

            return [(path, t)]
        output = []
        for dir in ld:  # 文件夹内有多个插件时
            output.extend(self.plugin_list(os.path.join(path, dir)))
        output = [x for x in output if x != None]
        return output

    def plugin_loaded(self):  # 已加载的插件
        output = []
        for l in list(self.lib.values()):
            output.append(l._path)
        for l in list(self.plugins.values()):
            output.append(l._path)
        return output

    def plugin_set(self, plugin: str, run=None):  # 加载插件
        if not os.path.exists(plugin):
            raise FileNotFoundError("Plugin does not exist")
        if os.path.isfile(plugin):  # 当插件为单个文件时
            self._add_plugin(
                open(plugin, encoding="utf-8").read(), run=run)
        else:  # 当插件为文件夹时
            if os.path.exists(plugin+"\\plugin.json"):  # 为单独的插件文件夹时
                plugin_file = json.load(
                    open(plugin+"\\plugin.json", encoding="utf-8"))
                if "name" in plugin_file:
                    name = plugin_file["name"]
                else:
                    name = None
                if "type" in plugin_file:
                    if plugin_file["type"] == "lib":
                        if "key" in plugin_file:
                            self._add_lib(
                                os.path.join(plugin, plugin_file["mainFile"]), key=plugin_file["key"])  # 加载库
                        else:
                            self._add_lib(
                                os.path.join(plugin, plugin_file["mainFile"]))
                    elif plugin_file["type"] == "plugin":
                        self._add_plugin(os.path.join(
                            plugin, plugin_file["mainFile"]), name=name, run=run)  # 加载插件
                else:
                    self._add_plugin(os.path.join(
                        plugin, plugin_file["mainFile"]), name=name, run=run)

    def plugin_more(self, paths):
        plugins_l = []
        for path in paths:
            plugins_l.extend(self.plugin_list(path))  # 获取要加载的插件列表
        mp = list(set(plugins_l)-set(self.plugin_loaded()))
        mp.sort(key=lambda x: x[1])
        return mp

    def reload(self):  # 重载
        self.__init__()
