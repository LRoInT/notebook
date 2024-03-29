import os
import tkinter
from tkinter import *
import easygui as eg
from main import *


"""class FormGUI:
    def __init__(self,form: book.form2d):
        self.form=form"""


class NoteBookGUI:  # 窗口类

    def __init__(self, notebook: book.NoteBook):
        self.notebook = notebook
        self.root = tkinter.Tk()  # 设置 TK窗口
        self.widget_dict = {  # 控件字典
            "other_widget": []  # 其它控件
        }
        self.config = {"save": "", "plugins": []}

    def __str__(self) -> str:
        return f"NoteBookGUI:(notebook:{self.notebook},size:{self.root.geometry()})"

    def __repr__(self) -> str:
        return self.__str__()

    def widget_init(self):
        self.widget_dict["other_widget"] = [
            # [控件,(relx,rely)]
            [Button(self.root, text="配置", command=self.config_set), (0.15, 0.85)],
            [Menu(self.root, tearoff=0),(0.05,0.4)],
        ]

    def load_widget(self, input_widget):
        widget, place = input_widget[:2]
        widget.place(relx=place[0], rely=place[1])

    def windows_init(self):
        self.root.title("快速笔记本")
        # self.root.geometry("1000x600")
        self.root.attributes()
        self.widget_init()  # 控件初始化
        self.mainFrame = Frame(self.root, width=800,
                               height=450, relief='groove', bd=2)  # 主界面
        # 填充常规控件
        for widget in self.widget_dict["other_widget"]:
            self.load_widget(widget)

        self.mainFrame.place(relx=0.15, rely=0.05, anchor="nw")
        self.root.mainloop()

    def config_check(self, config):
        history, save, plugins = config
        if os.path.exists(history):  # 检查路径
            back = self.notebook.history_set(history)  # 设置历史
            if back == 1:
                eg.msgbox("历史路径不为目录", title="配置错误")
        else:
            if history != "":
                eg.msgbox("历史文件不存在", title="配置错误")
        self.notebook.save_set(save)  # 设置保存
        for p in plugins.split(","):  # 分割插件列表
            if os.path.exists(p):  # 检查路径
                self.notebook.plugin_set(p)
            else:
                if p != "":
                    eg.msgbox(f"{p}插件不存在", title="配置错误")

    def config_set(self):  # 设置配置
        input_config = eg.multenterbox(
            "请输入配置", "配置输入", ["加载历史文件", "记录保存位置", "加载插件文件"], values=["", self.config["save"], ",".join(self.config["plugins"])])
        self.config_check(input_config)

    def run(self):
        self.windows_init()
