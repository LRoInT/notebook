import json
import tkinter as tk
from tkinter import *
import easygui as eg

from main import *

def menu_init(root):
        root.option_menu = Menu(root.root)  # 主菜单
        root.plugins_menu = Menu(root.option_menu)
        root.option_menu.add_cascade(
            label="插件", menu=root.plugins_menu)  # 插件菜单
        for p in root.notebook.plugins:  # 加载插件菜单
            root.plugins_menu.add_command(
                label=p, command=root.notebook.plugins[p][0].main)
        root.root.config(menu=root.option_menu)  # 设置菜单

if __name__ == "__main__":
    dconfig = json.load(open("./.config.json", encoding="utf-8"))  # 加载默认配置
    input_config = eg.multenterbox(  # 输入配置
        "请输入配置", "配置输入", ["记录保存位置", "加载插件文件"], values=[dconfig["save"], "".join(dconfig["plugins"])])
    # 类初始化
    notebook = book.NoteBook()
    bookgui = gui.NoteBookGUI(
        notebook, title=dconfig["name"], size=dconfig["size"], config=input_config)
    bookgui.run()
