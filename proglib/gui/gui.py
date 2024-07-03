import tkinter
from tkinter import *
from typing import Union
import easygui as eg
from proglib import book


class NoteBookGUI:  # 窗口类

    def __init__(self, notebook: book.NoteBook, title="NoteBook", size="1000x800", config={"save": "", "plugins": []}):
        self.notebook = notebook
        self.root = tkinter.Tk()  # 设置 TK窗口
        self.root.title(title)
        self.root.geometry(size)
        self.widget_dict = {  # 控件字典
            "other_widget": []  # 其它控件
        }
        config = {"save": config["save"], "plugins": config["plugins"]}
        self.defaultconfig = config
        self.config = config.copy()

    def __str__(self) -> str:
        return f"NoteBookGUI:(notebook={self.notebook},size={self.root.geometry()},config={self.config})"

    def __repr__(self) -> str:
        return self.__str__()

    def error_trans(self, e):  # 错误翻译
        return e

    def plugin2menu(self, menu, name, p, func):
        func = self.notebook.plugin_back_func(p)
        menu.add_command(  # 添加插件菜单选项
            label=name, command=func)

    def config_input(self, config: dict):
        save, plugins = config["save"], config["plugins"]
        self.notebook.save_set(save)  # 设置保存
        plugins_l = []
        for path in plugins:
            plugins_l.extend(self.notebook.plugin_list(path))
        sorted(plugins_l, key=lambda x: x[0])
        for p in plugins_l:  # 分割插件列表
            try:
                self.notebook.plugin_set(p[0], run=self)
            except Exception as e:
                e = self.error_trans(e)
                eg.msgbox(f"{e}", title="Plugin Load Error")

    def load_widget(self, input_widget: Union[tuple | list]):
        widget, place = input_widget
        widget.place(relx=place[0], rely=place[1])

    """def widget_init(self):  # 控件初始化
        self.option_menu = Menu(self.root)  # 主菜单
        self.file_menu = Menu(self.option_menu)  # 文件菜单
        self.option_menu.add_cascade(menu=self.file_menu, label="文件")  # 添加子菜单
        self.plugins_menu = Menu(self.option_menu)  # 插件菜单
        self.option_menu.add_cascade(menu=self.plugins_menu, label="插件")
        self.root.config(menu=self.option_menu)  # 设置菜单
    """

    def windows_init(self):  # 窗口布局初始化
        self.mainFrame = Frame(self.root)  # 主界面
        self.notebook.lib["mainlib"].init.gui_init(self)

    def run(self):
        # self.widget_init()  # 控件初始化
        self.windows_init()  # 窗口初始化
        self.config_input(self.config)
        self.root.mainloop()
