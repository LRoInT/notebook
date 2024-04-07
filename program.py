import json
import tkinter as tk
from tkinter import *
import easygui as eg

from proglib import book,gui


if __name__ == "__main__":
    dconfig = json.load(open("./.config.json", encoding="utf-8"))  # 加载默认配置
    # 类初始化
    notebook = book.NoteBook()
    bookgui = gui.NoteBookGUI(
        notebook, title=dconfig["name"], size=dconfig["size"], config=dconfig)
    bookgui.run()
    