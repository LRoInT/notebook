import tkinter
from tkinter import *
from typing import Union
import easygui as eg
from proglib import book


class NoteBookGUI:  # 窗口类

    def __init__(self, notebook: book.NoteBook, title, size, config):
        self.notebook = notebook
        self.root = tkinter.Tk()  # 设置 TK窗口
        self.root.title(title)
        self.root.geometry(size)
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
        mp = self.notebook.plugin_more(paths)

        for p in mp:  # 分割插件列表
            try:
                self.notebook.plugin_set(p[0], run=self)
            except Exception as e:  # 返回错误
                e = self.error_trans(e)
                eg.msgbox(f"{e}", title="Plugin Load Error")

    def load_widget(self, input_widget: Union[tuple | list]):
        widget, place = input_widget
        widget.place(relx=place[0], rely=place[1])

    def gui_init(self):
        self.option_menu = Menu(self.root)  # 主菜单
        self.file_menu = Menu(self.option_menu)  # 文件菜单
        self.option_menu.add_cascade(menu=self.file_menu, label="文件")  # 添加子菜单
        self.plugins_menu = Menu(self.option_menu)  # 插件菜单
        self.option_menu.add_cascade(menu=self.plugins_menu, label="插件")
        self.config_menu = Menu(self.option_menu)
        self.option_menu.add_cascade(menu=self.config_menu, label="设置")
        self.root.config(menu=self.option_menu)  # 设置菜单
        # ---
        self.mainFrame = Frame(self.root,)  # 主界面
        self.mainFrame.place(relx=0.05, rely=0.05,
                             relwidth=0.9, relheight=0.8, anchor="nw")

    def reload(self):
        self.root.destroy()
        

    def run(self, func=None):
        self.gui_init()
        self.config_input(self.config)
        if func is not None:
            func()
        self.root.mainloop()  # 进入主循环
