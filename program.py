import json
import tkinter as tk
from tkinter import *
import easygui as eg

from main import *


if __name__ == "__main__":
    dconfig = json.load(open("./.config.json", encoding="utf-8"))  # 加载默认配置
    input_config = eg.multenterbox(  # 输入配置
        "请输入配置", "配置输入", ["记录保存位置", "加载插件文件"], values=[dconfig["save"], "".join(dconfig["plugins"])])
    # 类初始化
    notebook = book.NoteBook()
    bookgui = gui.NoteBookGUI(
        notebook, title=dconfig["name"], size=dconfig["size"], config=input_config)
    bookgui.run()
