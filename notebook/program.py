import json
import os

import easygui
from proglib import book, gui


def rmdir(path):
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            os.remove(os.path.join(path, f))
        elif os.path.isdir(os.path.join(path, f)):
            rmdir(os.path.join(path, f))
    os.rmdir(path)


def show():
    show_text = []
    show_text.append("NoteBook:")
    show_text.append("文本:")
    for t in notebook.text:
        show_text.append(f"{t} -> {notebook.text[t]}")
    show_text.append("变量:")
    for v in notebook.var_group:
        show_text.append(f"{v} -> {notebook.var_group[v]}")
    show_text.append("插件:")
    for p in notebook.plugins:
        show_text.append(
            f"{p} -> {os.path.dirname(notebook.plugins[p]._path)}")
    easygui.msgbox("\n\n".join(show_text), "NoteBook信息")


def about():
    easygui.msgbox(
        "欢迎使用NoteBook\n\n本项目所属权归 卢茂宸 所有\n除部分库外,所有代码均为作者个人编写", "NoteBook")


def gui_run():  # 在窗口进入主循环前运行
    bookgui.option_menu.add_command(label="重载", command=bookgui.reload)
    bookgui.option_menu.add_command(label="当前信息", command=show)
    bookgui.option_menu.add_command(label="关于", command=about)
    notebook.note_set("./tdir")


if __name__ == "__main__":
    about()
    dconfig = json.load(open("./.config.json", encoding="utf-8"))  # 加载默认配置
    # 类初始化
    notebook = book.NoteBook()
    bookgui = gui.NoteBookGUI(
        notebook, title=dconfig["name"], size=dconfig["size"], config=dconfig)
    bookgui.run(gui_run)
