import json
from proglib import book,gui

def gui_run():
    notebook.lib["mainlib"].NBWelcome(bookgui)

if __name__ == "__main__":
    dconfig = json.load(open("./.config.json", encoding="utf-8"))  # 加载默认配置
    # 类初始化
    notebook = book.NoteBook()
    bookgui = gui.NoteBookGUI(
        notebook, title=dconfig["name"], size=dconfig["size"], config=dconfig)
    bookgui.run(gui_run)
    
