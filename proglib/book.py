import json
import os
import atexit
import sys
import re


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
        return f"NBPlugin:(plugin={self.pclass}, info={self.info})"


class NoteBook:  # 程序核心类
    def __init__(self):
        self.text = ""  # 文本
        self.val_group = {}  # 变量组
        self.save = None  # 保存
        self.plugins = {}  # 查检字典
        self.lib = {}  # 支持库
        self.inuse = None  # 运行插件

    def __str__(self):
        return f"NoteBook(text={self.text}, val_group={self.val_group}, plugins={self.plugins})"

    def __repr__(self):
        return self.__str__()

    def output_save(self):
        json.dump(self.val_group, open(os.path.join(
            self.save, "val_group.json"), "w"),  indent=4, ensure_ascii=False)
        open(os.path.join(self.save, "text.txt"), "w").write(self.text)

    def history_set(self, path):
        if not os.path.isdir(path):
            return 1
        self.text = open(os.path.join(path, "text.txt")).read()
        self.val_group = json.load(
            open(os.path.join(path, "val_group.json"), encoding="utf-8"))

    def save_set(self, path):  # 保存设置
        if type(path) == list:  # 当输入多个路径时
            for p in path:
                self.config_set(p)
        if path == "":  # 不保存
            self.save = None
            try:
                atexit.unregister(self.output_save)  # 取消自动保存
            except:
                pass
        if os.path.exists(path):  # 检查路径是否存在
            self.save = path
            atexit.register(self.output_save)  # 开启自动保存
        else:
            try:
                os.mkdir(path)
            finally:
                self.save = path
                atexit.register(self.output_save)  # 开启自动保存

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
        scope = {}  # 设置作用域
        exec(open(path, encoding="utf-8").read(), scope)  # 初始化插件
        scope.pop('__builtins__')
        if name == None:  # 设置插件名称
            name = scope["name"]

        if name in self.plugins:
            return None
        plugin_l = {}
        try:
            p = scope[name+"Run"](run)
        except Exception as e:
            raise RuntimeError(
                f"Plugin({path}) {e}")
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
            if "type" in t:
                if t["type"] == "lib":  # 插件类型为库时
                    t = 0
                elif t["type"] == "plugin":  # 插件类型为功能型插件时
                    t = 1
                else:
                    t = 1
            else:
                t = 1

            return [(path, t)]
        output = []
        for dir in ld:  # 文件夹内有多个插件时
            output.extend(self.plugin_list(os.path.join(path, dir)))
        return output

    def plugin_loaded(self):
        output = []
        for l in list(self.lib.values()):
            output.append(l._path)
        for l in list(self.plugins.values()):
            output.append(l._path)
        return output

    def plugin_set(self, plugin, run=None):  # 加载插件
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
