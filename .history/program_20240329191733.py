import json
import tkinter as tk
from tkinter import *
import easygui as eg

from main import *

def menu_init(self):
        self.option_menu = Menu(self.root)  # 主菜单
        self.plugins_menu = Menu(self.option_menu)
        self.option_menu.add_cascade(
            label="插件", menu=self.plugins_menu)  # 插件菜单
        for p in self.notebook.plugins:  # 加载插件菜单
            self.plugins_menu.add_command(
                label=p, command=self.notebook.plugins[p][0].main)
        self.root.config(menu=self.option_menu)  # 设置菜单

if __name__ == "__main__":
    dconfig = json.load(open("./.config.json", encoding="utf-8"))  # 加载默认配置
    input_config = eg.multenterbox(  # 输入配置
        "请输入配置", "配置输入", ["记录保存位置", "加载插件文件"], values=[dconfig["save"], "".join(dconfig["plugins"])])
    # 类初始化
    notebook = book.NoteBook()
    bookgui = gui.NoteBookGUI(
        notebook, title=dconfig["name"], size=dconfig["size"], config=input_config)
    bookgui.run()
