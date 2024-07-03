import os
import tkinter
from tkinter import *
from typing import Union
import easygui as eg
from proglib import book


class NoteBookGUI:  # 窗口类
    def __init__(self, notebook: book.NoteBook, title, size, config):
        self.notebook = notebook
        self.root = tkinter.Tk()  # 设置 TK窗口
        self.root.title(title)  # 设置标题
        if type(size) == str:  # 设置窗口大小
            self.root.geometry(size)
        elif type(size) == list:
            win_width, win_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
            self.root.geometry(
                f"{int(size[0]*win_width)}x{int(size[1]*win_height)}")
        self.defaultconfig = config
        self.config = config.copy()

    def __str__(self) -> str:
        return f"NoteBookGUI:(notebook={self.notebook},size={self.root.geometry()},config={self.config})"

    def __repr__(self) -> str:
        return self.__str__()

    def error_trans(self, e):  # 错误翻译
        return e

    def plugin2menu(self, name, p, menu):
        func = self.notebook.plugin_back_func(p)
        menu.add_command(  # 添加插件菜单选项
            label=name, command=func)

    def config_input(self, config: dict):
        save, plugins = config["save"], config["plugins"]
        self.notebook.save_set(save)  # 设置保存
        self.plugin_load(plugins)

    def plugin_load(self, paths):  # 加载插件
        plugins = []
        for p in paths:  # 遍历插件路径
            if os.path.exists(p):  # 判断插件是否存在
                plugins.extend(self.notebook.plugin_list(p))
        for p in plugins:  # 分割插件列表
            try:
                self.notebook.plugin_set(p[0], run=self)
            except:  # 返回错误
                eg.exceptionbox()

    def gui_init(self):
        self.option_menu = Menu(self.root)  # 主菜单
        self.file_menu = Menu(self.option_menu)  # 文件菜单
        self.option_menu.add_cascade(menu=self.file_menu, label="文件")  # 添加子菜单
        self.plugins_menu = Menu(self.option_menu)  # 插件菜单
        self.option_menu.add_cascade(menu=self.plugins_menu, label="工具")
        self.config_menu = Menu(self.option_menu)
        self.option_menu.add_cascade(menu=self.config_menu, label="设置")
        self.root.config(menu=self.option_menu)  # 设置菜单
        # ---
        self.mainFrame = Frame(self.root, relief="groove")  # 主界面
        self.mainFrame.place(relx=0.49, rely=0.5, relwidth=0.98,
                             relheight=0.95, anchor="center")

    def reload(self):  # 重载
        self.root.destroy()  # 关闭窗口
        self.notebook.reload()  # 重载 notebook
        title = self.defaultconfig["title"]
        size = self.defaultconfig["size"]
        self.__init__(self.notebook, title, size, self.defaultconfig)
        self.run(self.func)

    def run(self, func=None):
        self.gui_init()
        self.config_input(self.config)
        if func != None:
            self.func = func
            func()
        else:
            self.func = lambda: None
        self.root.mainloop()  # 进入主循环
