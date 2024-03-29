import json
import easygui as eg
from main import *
defaultconfig = json.load(open("./.config.json", encoding="utf-8"))
input_config = eg.multenterbox(
    "请输入配置", "配置输入", ["加载历史文件", "记录保存位置", "加载插件文件"], values=["", defaultconfig["save"], ""])
notebook = book.NoteBook()
bookgui = gui.NoteBookGUI(notebook)
bookgui.config["plugins"].append("/.plugins")
bookgui.run()
