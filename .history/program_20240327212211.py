import json
import easygui as eg
from main import *
dconfig = json.load(open("./.config.json", encoding="utf-8"))
input_config = eg.multenterbox(
    "请输入配置", "配置输入", ["加载历史文件", "记录保存位置", "加载插件文件"], values=["", dconfig["save"], "".join(dconfig["plugins"])])
input_config{"save":input_config["save"],"plugins":input_config["plugins"].split(",")}
notebook = book.NoteBook()
bookgui = gui.NoteBookGUI(notebook,title=dconfig["name"],size=dconfig["size"],config=input_config)
bookgui.run()
