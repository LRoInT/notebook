import tkinter as tk
from tkinter import *
from tkinter import ttk


class NBTextEditon:  # 文本编辑器
    def __init__(self, nb):
        self.gui = nb
        self.nb = nb.notebook
        self.chose_box = ttk.Combobox(
            self.gui.mainFrame, values=list(self.nb.text.keys()))
        self.chose_box.bind("<<ComboboxSelected>>", self.on_select)  # 选择事件
        self.chose_box.bind("<Return>", self.on_select)  # 输入事件
        self.text_box = tk.Text(self.gui.mainFrame)
        self.save_b = Button(text="保存文本", command=self.st)

    def on_select(self, event):  # 选择事件
        widget = event.widget
        get_val = widget.get()
        if get_val not in self.nb.text:
            self.nb.text_add(get_val, text="", path=(
                (self.nb.save[0] if self.nb.save[0] != None else "./.temp"), f"{get_val}.txt"), mode="w+")
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.INSERT, f"{self.nb.text[get_val].text}")
        self.chose_box["values"] = tuple(self.nb.text.keys())

    def st(self):
        if self.chose_box.get() not in self.nb.text:
            return None
        else:
            self.nb.text[self.chose_box.get()].input(self.text_box.get(
                1.0, tk.END))
            self.nb.text[self.chose_box.get()].save()

    def main(self):
        self.chose_box["values"] = tuple(self.nb.text.keys())
        self.chose_box.place(relx=0.15, rely=0.05,
                             relwidth=0.3, relheight=0.05)
        self.text_box.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.8)
        self.save_b.place(relx=0.5, rely=0.05,
                          relwidth=0.05, relheight=0.05)

    def quit(self):
        self.chose_box.place_forget()
        self.text_box.place_forget()
        self.save_b.place_forget()


class NBValEditon:  # 变量表编辑器
    def __init__(self, nb):
        self.gui = nb
        self.nb = nb.notebook
        self.chose_box1 = ttk.Combobox(  # 选择变量组
            self.gui.mainFrame, values=list(self.nb.var_group.keys()))
        self.chose_box1.bind("<<ComboboxSelected>>", self.chose_group)  # 选择事件
        self.chose_box2 = ttk.Combobox(  # 选择变量
            self.gui.mainFrame)
        self.chose_box2.bind("<<ComboboxSelected>>", self.chose_var)
        self.val = Text(self.gui.mainFrame)
        

    def chose_group(self, event):
        widget = event.widget
        get_val = widget.get()
        self.open_group=get_val
        if get_val not in self.nb.var_group:
            self.nb.var_group_add(get_val, var_group=None)
        self.chose_box2["values"] = tuple(
            self.nb.var_group[get_val].vars.keys())
        self.val.delete("1.0", tk.END)
    
    def chose_var(self, event):
        widget = event.widget
        get_val = widget.get()
        if get_val not in self.nb.var_group[self.open_group].vars:
            self.nb.var_group[self.open_group].add(get_val, value=0)
        self.val.delete("1.0", tk.END)
        self.val.insert(tk.INSERT, f"{self.nb.var_group[self.open_group].vars[get_val].value}")
        

    def main(self):
        self.chose_box1["values"] = tuple(self.nb.var_group.keys())
        self.open_group=self.chose_box1["values"][0]
        self.chose_box1.pack()
        self.chose_box2.pack()
        self.val.pack()

    def quit(self):
        self.chose_box1.pack_forget()
        self.chose_box2.pack_forget()
        self.val.pack_forget()
