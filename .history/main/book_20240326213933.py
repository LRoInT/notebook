import json
import os
import atexit
import sys
import numpy as np
import re

"""get_word = re.compile("[a-zA-Z]")  # 获取字母
def wordintext(t): return "".join(get_word.findall(t)).lower()


get_num = re.compile("[0-9]")  # 获取数字
def numintext(t): return int("".join(get_num.findall(t)))


def title2num(text):
    words = 'abcdefghijklmnopqrstuvwxyz'
    text = wordintext(text)
    ct = text[::-1]
    if len(text) == 1:
        return words.find(text)
    else:
        num = 0
        for i in range(len(text)):
            num += 26**i*(words.find(ct[i])+1)
    return num


class form_cell:  # 单元格类
    def __init__(self, data, type="int", style="no"):
        self.data = data
        self.type = type
        self.style = style

    def __str__(self):
        return f"Form_cell(data={self.data}, type={self.type}, style={self.style})"

    def __repr__(self):
        return self.__str__()


class form2d:  # 表格类
    def __init__(self, object=[[]]) -> None:
        for i in range(len(object)):
            for j in range(len(object[i])):
                if isinstance(object[i][j], (list, tuple)):
                    raise TypeError("Nested lists are not allowed in tables")
                object[i][j] = form_cell(j)
        self.form = np.array(object)

    def __getitem__(self, index):
        if type(index) == str:
            line = numintext(index)-1  # 行
            column = title2num(index)  # 列

            return self.form[line, column]"""


class NoteBook:
    def __init__(self):
        self.text = ""  # 文本
        self.val_group = {}  # 变量组
        self.save = None
        self.plugins = {}

    def __str__(self):
        return f"NoteBook(save={self.save}, text={self.text}, val_group={self.val_group})"

    def __repr__(self):
        return self.__str__()

    def output_save(self):
        json.dump(os.path.join(
            self.save, "val_group.json"), self.val_group, indent=4, ensure_ascii=False)
        open(os.path.join(self.save, "text.txt")).write(self.text)

    def save_set(self, path):  # 保存设置
        if type(path) == list:  # 当输入多个路径时
            for p in path:
                self.config_set(p)
        if path == "":  # 不保存
            self.save = None
            try:
                atexit.unregister(self.output_save)
            except:
                pass
            return True
        if os.path.exists(path):  # 检查路径是否存在
            self.save = path
            atexit.register(self.output_save)  # 开启自动保存
            return True
        else:
            return False

    def _add_plugin(self, plugin_code,name=None):
        scope = {}  # 设置作用域
        exec(plugin_code, scope)
        if name ==None:plugin_code=name
        else:plugin_name=scope["name"]
        self.plugins[plugin_name] = []
        self.plugins[plugin_name].append(scope[plugin_name+"Run"]())
        if "__other__" in scope:
            for a in scope["__other__"]:
                self.plugins[plugin_name].append(scope[a])
        

    def plugin_set(self, plugin):
        if os.path.exists(plugin):  # 确认文件存在
            if os.path.isfile(plugin):  # 当插件为单个文件时
                name, code = self._add_plugin(
                    open(plugin, encoding="utf-8").read())
                self.plugins[name] = code
                return True
            else:  # 当插件为文件夹时
                if os.path.exists(plugin+"\\plugin.json"):
                    plugin_file = json.load(
                        open(plugin+"\\plugin.json", encoding="utf-8"))
                    if "name" in plugin_file:name=plugin_file["name"]
                    else:name=None
                    self._add_plugin(open(plugin+"\\"+plugin_file["code"], encoding="utf-8").read(),name=name)
                else:
                    for dir in os.listdir(plugin):
                        self.plugin_set(plugin+"\\"+dir)

        else:
            raise FileNotFoundError
