import json
import os
import atexit
import sys
import re


class NoteBook:
    def __init__(self):
        self.text = ""  # 文本
        self.val_group = {}  # 变量组
        self.save = None
        self.plugins = {}

    def __str__(self):
        return f"NoteBook(save={self.save}, text={self.text}, val_group={self.val_group},plugins={self.plugins})"

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

    def _add_plugin(self, plugin_code, name=None,run=None):
        if run is None:
            run=self
        scope = {}  # 设置作用域
        exec(plugin_code, scope)
        if name == None:  # 设置插件名称
            plugin_name = scope["name"]
        else:
            plugin_name = name
        if name in self.plugins:
            return None
        self.plugins[plugin_name] = []
        self.plugins[plugin_name].append(scope[plugin_name+"Run"](run))  # 插件类
        if "__other__" in scope:  # 添加其他信息
            for a in scope["__other__"]:
                self.plugins[plugin_name].append(scope[a])

    def plugin_set(self, plugin,run):
        if os.path.isfile(plugin):  # 当插件为单个文件时
            self._add_plugin(
                open(plugin, encoding="utf-8").read(),run=run)
        else:  # 当插件为文件夹时
            if os.path.exists(plugin+"\\plugin.json"):  # 为单独的插件文件夹时
                plugin_file = json.load(
                    open(plugin+"\\plugin.json", encoding="utf-8"))
                if "name" in plugin_file:
                    name = plugin_file["name"]
                else:
                    name = None
                self._add_plugin(  # 添加插件
                    open(plugin+"\\"+plugin_file["mainFile"], encoding="utf-8").read(), name=name,run=run)
            else:
                for dir in os.listdir(plugin):  # 文件夹内有多个插件时
                    self.plugin_set(plugin+"\\"+dir)
