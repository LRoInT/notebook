import os
import tkinter
from tkinter import *
from typing import Union
import easygui as eg
from main import *


class NoteBookGUI:  # 窗口类

    def __init__(self, notebook: book.NoteBook, title="NoteBook", size="1000x800", config={"save": "", "plugins": []}):
        self.notebook = notebook
        self.root = tkinter.Tk()  # 设置 TK窗口
        self.root.title(title)
        self.root.geometry(size)
        self.widget_dict = {  # 控件字典
            "other_widget": []  # 其它控件
        }
        self.config_input(config)  # 加载配置
        config = {"save": config[0], "plugins": config[1].split(",")}
        self.defaultconfig = config
        self.config = config.copy()

    def __str__(self) -> str:
        return f"NoteBookGUI:(notebook={self.notebook},size={self.root.geometry()},config={self.config})"

    def __repr__(self) -> str:
        return self.__str__()

    def config_set(self):  # 设置配置
        input_config = eg.multenterbox(
            "请输入配置", "配置输入", ["记录保存位置", "加载插件文件"], values=[self.config["save"], ",".join(self.config["plugins"])])
        self.config_input(input_config)

    def config_input(self, config: list):
        save, plugins = config
        self.notebook.save_set(save)  # 设置保存
        for p in plugins.split(","):  # 分割插件列表
            if os.path.exists(p):  # 检查路径
                self.notebook.plugin_set(p,scope={self})
            else:
                if p != "":
                    eg.msgbox(f"{p}插件不存在", title="配置错误")

    def widget_init(self):
        self.widget_dict["other_widget"] = [
            # [控件,(relx,rely)]
            [Button(self.root, text="配置", command=self.config_set), (0.15, 0.85)]
        ]

    def load_widget(self, input_widget: Union[tuple | list]):
        widget, place = input_widget
        widget.place(relx=place[0], rely=place[1])

    def menu_init(self):
        self.option_menu = Menu(self.root)  # 主菜单
        self.plugins_menu = Menu(self.option_menu)
        self.option_menu.add_cascade(
            label="插件", menu=self.plugins_menu)  # 插件菜单
        for p in self.notebook.plugins:  # 加载插件菜单
            self.plugins_menu.add_command(
                label=p, command=self.notebook.plugins[p][0].main)
        self.root.config(menu=self.option_menu)  # 设置菜单

    def windows_init(self):
        self.widget_init()  # 控件初始化
        self.menu_init()  # 菜单初始化

        self.mainFrame = Frame(self.root, width=800,
                               height=450, relief='groove', bd=2)  # 主界面
        # 填充常规控件
        for widget in self.widget_dict["other_widget"]:
            self.load_widget(widget)

        self.mainFrame.place(relx=0.15, rely=0.05, anchor="nw")
        self.root.mainloop()

    def run(self):
        self.windows_init()
