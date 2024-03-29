import easygui
from main import *
input_config = eg.multenterbox(
            "请输入配置", "配置输入", ["加载历史文件", "记录保存位置", "加载插件文件"], values=["", self.config["save"], ",".join(self.config["plugins"])])
notebook=book.NoteBook()
bookgui=gui.NoteBookGUI(notebook)
bookgui.config["plugins"].append("/.plugins")
bookgui.run()