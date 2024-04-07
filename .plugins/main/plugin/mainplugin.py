import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
import easygui


class NBTextEditon:  # 文本编辑器
    def __init__(self, nb):
        self.gui = nb
        self.nb = nb.notebook
        self.textin = tk.Text(self.gui.mainFrame)
        self.textin.insert(tk.INSERT, self.nb.text)

        self.save_b = tk.Button(
            self.gui.mainFrame, text="save", command=self.st)

    def st(self):
        self.nb.text = self.textin.get("1.0", tk.END)

    def main(self):
        self.textin.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)
        self.save_b.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.2)

    def quit(self):
        self.textin.place_forget()
        self.save_b.place_forget()


class NBValEditon:  # 变量表编辑器
    def __init__(self, nb):
        self.gui = nb
        self.nb = nb.notebook
        self.nblib = self.nb.lib
        self.val = self.nb.val_group
        self.val_text = tk.Text(self.gui.mainFrame)
        self.save_b = tk.Button(
            self.gui.mainFrame, text="save", command=self.st)
        self.combobox = ttk.Combobox(
            self.gui.mainFrame, values=list(self.val.keys()).sort())  # 多选框
        self.open = None
        self.combobox.bind("<<ComboboxSelected>>", self.on_select)  # 选择事件
        self.combobox.bind("<Return>", self.on_select)  # 输入事件

    def st(self):
        if self.open is None:
            return None
        else:
            self.val[self.open] = self.val_text.get(1.0, tk.END)

    def on_select(self, event):
        widget = event.widget
        get_val = widget.get()
        self.val_text.delete("1.0", tk.END)
        if get_val not in self.val:
            self.val[get_val] = ""
        else:
            self.val_text.insert(tk.INSERT, f"{self.val[get_val]}")
        self.open = get_val
        self.combobox.config(values=list(self.val.keys()))

    def main(self):
        self.val_name.place(relx=0.2, rely=0.2,
                            relwidth=0.2, relheight=0.2)
        self.save_b.place(relx=0.2, rely=0.8,
                          relwidth=0.2, relheight=0.2)
        self.combobox.place(relx=0.2, rely=0.6,
                            relwidth=0.6, relheight=0.2)
        self.val_text.pack()

    def quit(self):
        self.val_name.place_forget()
        self.combobox.place_forget()
        self.val_text.pack_forget()


class mainpluginRun:
    def __init__(self, nb):
        self.gui = nb
        self.nb = nb.notebook
        self.te = NBTextEditon(self.gui)
        self.gui.plugin2menu("文本编辑器", self.te, self.gui.plugins_menu)
        self.ve = NBValEditon(self.gui)
        self.gui.plugin2menu("变量编辑器", self.ve, self.gui.plugins_menu)
        self.gui.file_menu.add_command(label="加载文件", command=self.load_file)
        self.nb.lib["mainlib"].NBWelcome(self.gui)

    def _load_file(self, path):
        self.nb.plugin_quit()
        self.nb.history_set(path)
        self.nb.lib["mainlib"].NBWelcome(self.gui)

    def load_file(self):
        path = easygui.diropenbox(title="选择文件夹")
        if os.path.exists(path):
            if bool(self.nb.text) or bool(self.nb.val_group):
                chose = easygui.ccbox(
                    "加载文件将会清空当前内容\n是否加载", choices=["加载", "取消"], title="警告")
                if chose:
                    self._load_file(path)
            else:
                self._load_file(path)
        else:
            easygui.msgbox("文件不存在", "错误")
