import json
import os
from proglib import book, gui


def rmdir(path):
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            os.remove(os.path.join(path, f))
        elif os.path.isdir(os.path.join(path, f)):
            rmdir(os.path.join(path, f))
    os.rmdir(path)


def clean_temp():  # 清理临时文件
    if os.path.exists("./.temp"):
        rmdir("./.temp")


def gui_run():  # 在窗口进入主循环前运行
    clean_temp()
    bookgui.option_menu.add_command(label="重载", command=bookgui.reload)
    bookgui.option_menu.add_command(label="显示", command=lambda : print(bookgui))
    notebook.note_set("./tdir")
    notebook.lib["mainlib"].NBWelcome(bookgui)


if __name__ == "__main__":
    dconfig = json.load(open("./.config.json", encoding="utf-8"))  # 加载默认配置
    # 类初始化
    notebook = book.NoteBook()
    bookgui = gui.NoteBookGUI(
        notebook, title=dconfig["name"], size=dconfig["size"], config=dconfig)
    bookgui.run(gui_run)
    clean_temp()
