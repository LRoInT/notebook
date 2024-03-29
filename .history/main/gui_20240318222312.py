import tkinter
from tkinter import *
import easygui as eg
from main import *


class NoteBookGUI:  # 窗口类

    def __init__(self, notebook: book.Notebook):
        self.notebook = notebook
        self.widget_dict = {  # 控件字典
            "page_option": [],  # 选项列表
            "other_widget": []  # 其它控件
        }
        self.config = {}

    def __str__(self) -> str:
        return f"NoteBookGUI:(notebook:{self.notebook},size:{self.root.geometry()})"

    def __repr__(self) -> str:
        return self.__str__()

    def windows_init(self):
        self.root = tkinter.Tk()  # 设置 TK窗口
        self.root.title("快速笔记本")
        self.root.geometry("1000x600")
        self.optionFrame = Frame(self.root, width=100, height=500, bd=2)
        self.mainFrame = Frame(self.root, width=800, height=500, bd=2)  # 显示界面
        self.optionFrame.place(relx=0.05, rely=0.05, anchor="nw")
        for b in range(len(self.widget_dict["page_option"])):  # 填充控件
            self.widget_dict["page_option"].place(relx=0.1, rely=0.05+0.75*b)
        self.mainFrame.place(relx=0.05, rely=0.05, anchor="nw")
        self.root.mainloop()

    def config_set(self):  # 设置配置
        input_config = eg.multenterbox(
            "请输入配置", "配置输入", ["加载历史文件", "记录保存位置", "加载插件文件"], values=self.config.values())
        for c in input_config:
            self.config[c] = input_config[c]

    def run(self):
        self.windows_init()
