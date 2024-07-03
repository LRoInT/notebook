import ast
import os
from tkinter import ttk
from tkinter import *
import tkinter as tk

import easygui


class NBTextEditon:  # 文本编辑器
    def __init__(self, nb):
        self.gui = nb
        self.nb = nb.notebook
        self.chose_box = ttk.Combobox(
            self.gui.mainFrame, values=list(self.nb.text.keys()))
        self.chose_box.bind("<<ComboboxSelected>>", self.on_select)  # 选择事件
        self.chose_box.bind("<Return>", self.on_select)  # 输入事件
        self.text_box = tk.Text(self.gui.mainFrame)
        self.text_box.bind("<Control-s>", lambda x: self.st)
        self.text_box.bind("<Control-r>", lambda x: self.rename)
        self.text_box.bind("<Control-d>", lambda x: self.delete)
        self.text_box.bind("<Return>", lambda x: self.st)
        self.save_b = Button(text="保存文本", command=self.st)
        self.rename_b = Button(text="重命名", command=self.rename)
        self.delete_b = Button(text="删除", command=self.delete)

    def on_select(self, event):  # 选择事件
        widget = event.widget
        get_val = widget.get()
        if get_val not in self.nb.text:
            self.nb.text_add(get_val, text="", path=(
                (self.nb.save[0] if self.nb.save[0] != None else "./.temp"), f"{get_val}.txt"))
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

    def rename(self):
        old_name = self.chose_box.get()
        new_name = easygui.enterbox(
            title="重命名", msg="请输入新的名称", default=old_name)
        old_text = self.nb.text[old_name]
        file_name = old_text.root, f"{new_name}.txt"
        open(os.path.join(*file_name), "w")

        self.nb.text_add(new_name, text=old_text.text, path=file_name)
        self.nb.text[new_name].save()
        self.delete()
        self.chose_box["values"] = tuple(self.nb.text.keys())  # 刷新

    def delete(self):
        if self.chose_box.get() not in self.nb.text:
            return None
        else:
            text = self.chose_box.get()
            os.remove(self.nb.text[text].path if type(
                self.nb.text[text].path) != tuple else os.path.join(*self.nb.text[text].path))
            self.nb.text.pop(text)
            self.chose_box["values"] = tuple(self.nb.text.keys())

    def main(self):
        self.chose_box["values"] = tuple(self.nb.text.keys())
        self.chose_box.place(relx=0.15, rely=0.05,
                             relwidth=0.3, relheight=0.05)
        self.text_box.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.8)
        self.save_b.place(relx=0.5, rely=0.05,
                          relwidth=0.05, relheight=0.05)
        self.rename_b.place(relx=0.6, rely=0.05,
                            relwidth=0.05, relheight=0.05)
        self.delete_b.place(relx=0.7, rely=0.05,
                            relwidth=0.05, relheight=0.05)

    def quit(self):
        self.chose_box.place_forget()
        self.text_box.place_forget()
        self.save_b.place_forget()
        self.rename_b.place_forget()
        self.delete_b.place_forget()


# 名称对应类型
name2type_dict = {"自动(安全)": (ast.literal_eval, None), "自动(不安全)": (eval, None), "整数": (int, int), "浮点数": (float, float),
                  "字符串": (str, str), "布尔值": (bool, bool), "列表": (lambda x: eval(f"list({x})"), list), "字典": (lambda x: eval(f"dict({x})"), dict)}


class NBValEditon:  # 变量表编辑器
    def __init__(self, nb):
        self.gui = nb
        self.nb = nb.notebook
        self.chose_box1 = ttk.Combobox(  # 选择变量组
            self.gui.mainFrame, values=list(self.nb.var_group.keys()))
        self.chose_box1.bind("<<ComboboxSelected>>", self.chose_group)  # 选择事件
        self.chose_box1.bind("<Return>", self.chose_group)  # 选择事件
        self.chose_box2 = ttk.Combobox(  # 选择变量
            self.gui.mainFrame)
        self.chose_box2.bind("<<ComboboxSelected>>", self.chose_var)
        self.chose_box2.bind("<Return>", self.chose_var)
        self.val = Text(self.gui.mainFrame)
        self.save_b = Button(text="保存变量", command=self.sv)
        self.type_box = ttk.Combobox(
            self.gui.mainFrame
        )
        self.type_box.bind("<<ComboboxSelected>>", self.type_chose)
        self.name2type = name2type_dict
        self.type_box["values"] = list(self.name2type.keys())
        self.rename_group_b = Button(text="重命名变量组", command=self.rename_group)
        self.delete_group_b = Button(text="删除变量组", command=self.delete_group)
        self.rename_var_b = Button(text="重命名变量", command=self.rename_var)
        self.delete_var_b = Button(text="删除变量", command=self.delete_var)

    def sv(self):  # 保存变量
        var = self.nb.var_group[self.open_group].vars[self.chose_box2.get()]
        val = self.val.get("1.0", tk.END)
        t = self.type_box.get()
        # 类型转换
        if t == "":
            val = eval(val)
        if t in self.name2type:
            try:
                val = self.name2type[t][0](val)
            except:
                pass
        else:
            easygui.msgbox("请输入正确的类型", "类型错误")
            return 0
        var.input(val, 1)  # 输入
        self.type_box.set(self.type2name(var.type))
        self.val.delete("1.0", tk.END)
        self.val.insert(
            tk.INSERT, str(self.nb.var_group[self.open_group].vars[self.chose_box2.get()].value))

    def type2name(self, type):
        types = [i[1] for i in list(self.name2type.values())]
        if type in types:
            return list(self.name2type.keys())[types.index(type)]
        else:
            return str(type)[8:-2]

    def type_chose(self, event):  # 选择类型
        widget = event.widget
        get_val = widget.get()
        if get_val in self.name2type:
            var = self.name2type[get_val][0](self.val.get("1.0", tk.END))
            self.nb.var_group[self.open_group].vars[self.chose_box2.get()].type = type(
                var)
            self.val.delete("1.0", tk.END)
            self.val.insert(
                tk.INSERT, str(self.nb.var_group[self.open_group].vars[self.chose_box2.get()].value))

    def rename_group(self):  # 重命名变量组
        old_name = self.chose_box1.get()
        new_name = easygui.enterbox(
            title="重命名变量组", msg="请输入新的名称", default=old_name)
        if new_name is None:
            return 0
        old_group = self.nb.var_group[old_name]
        file_name = old_group.root, f"{new_name}.json"
        open(os.path.join(*file_name), "w")
        old_group.path = file_name
        self.delete_group()
        self.nb.var_group_add(new_name, vars=old_group.vars, path=file_name)
        self.chose_box1["values"] = tuple(self.nb.var_group.keys())  # 刷新
        self.chose_box1.set(new_name)

    def delete_group(self):  # 删除变量组
        if self.chose_box1.get() not in self.nb.var_group:
            return None
        else:
            group = self.chose_box1.get()
            os.remove(self.nb.var_group[group].path if type(
                self.nb.var_group[group].path) != tuple else os.path.join(*self.nb.var_group[group].path))
            self.nb.var_group.pop(group)
            self.chose_box1["values"] = tuple(self.nb.var_group.keys())
            self.chose_box1.set("")
            self.val.delete("1.0", tk.END)
            self.chose_box2["values"].set("")
            self.open_group = ""

    def rename_var(self):  # 重命名变量
        old_name = self.chose_box2.get()
        new_name = easygui.enterbox(
            title="重命名变量", msg="请输入新的名称", default=old_name)
        if new_name is None:
            return 0
        old_var = self.nb.var_group[self.open_group][old_name]
        self.nb.var_group[self.open_group].add(
            name=new_name, value=old_var.value)
        self.delete_var()
        self.chose_box2["values"] = tuple(
            self.nb.var_group[self.open_group].vars.keys())  # 刷新
        self.chose_box2.set(new_name)
        self.val.insert(
            tk.INSERT, str(self.nb.var_group[self.open_group].vars[new_name].value))

    def delete_var(self):  # 删除变量
        if self.chose_box2.get() not in self.nb.var_group[self.open_group].vars:
            return None
        else:
            var = self.chose_box2.get()
            self.nb.var_group[self.open_group].vars.pop(var)
            self.chose_box2["values"] = tuple(
                self.nb.var_group[self.open_group].vars.keys())
            self.chose_box2.set("")
            self.val.delete("1.0", tk.END)

    def chose_group(self, event):  # 选择变量组
        widget = event.widget
        get_val = widget.get()
        self.type_box.set("")
        self.open_group = get_val
        if get_val not in self.nb.var_group:
            self.nb.var_group_add(get_val, vars={}, path=[
                                  self.nb.save[0], f"{get_val}.json"])
            self.chose_box1["values"] = tuple(
                self.nb.var_group.keys()
            )
        self.chose_box2["values"] = list(
            self.nb.var_group[get_val].vars.keys())
        self.val.delete("1.0", tk.END)

    def chose_var(self, event):  # 选择变量
        widget = event.widget
        get_val = widget.get()
        if get_val not in self.nb.var_group[self.open_group].vars:  # 新建变量
            self.nb.var_group[self.open_group].add(name=get_val, value=0)
            self.chose_box2["values"] = tuple(
                self.nb.var_group[self.open_group].vars.keys()
            )
        self.type_box.set(
            self.type2name(type(self.nb.var_group[self.open_group].vars[get_val].value)))
        self.val.delete("1.0", tk.END)
        self.val.insert(
            tk.INSERT, str(self.nb.var_group[self.open_group].vars[get_val].value))

    def main(self):
        self.chose_box1["values"] = tuple(self.nb.var_group.keys())
        self.open_group = self.chose_box1["values"][0] if self.chose_box1["values"] else [
        ]
        self.chose_box1.place(relx=0.05, rely=0.05,
                              relwidth=0.2, relheight=0.05)
        self.chose_box2.place(relx=0.26, rely=0.05,
                              relwidth=0.2, relheight=0.05)
        self.val.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.8)
        self.save_b.place(relx=0.46, rely=0.06,
                          relwidth=0.05, relheight=0.05)
        self.type_box.place(relx=0.52, rely=0.05,
                            relwidth=0.2, relheight=0.05)
        self.type_box.set(list(self.name2type.keys())[0])
        self.rename_group_b.place(relx=0.72, rely=0.05,
                                  relwidth=0.06, relheight=0.05)
        self.delete_group_b.place(relx=0.72, rely=0.1,
                                  relwidth=0.06, relheight=0.05
                                  )
        self.rename_var_b.place(relx=0.8, rely=0.05,
                                relwidth=0.06, relheight=0.05)
        self.delete_var_b.place(relx=0.8, rely=0.1,
                                relwidth=0.06, relheight=0.05
                                )

    def quit(self):  # 退出
        self.chose_box1.place_forget()
        self.chose_box2.place_forget()
        self.val.place_forget()
        self.save_b.place_forget()
        self.type_box.place_forget()
        self.rename_group_b.place_forget()
        self.delete_group_b.place_forget()
        self.rename_var_b.place_forget()
        self.delete_var_b.place_forget()
