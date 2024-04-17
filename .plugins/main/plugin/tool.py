import os
from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
import easygui
import datetime


class iterateTool:
    def __init__(self, nb):
        self.gui = nb
        self.nb = nb.notebook
        self.mframe = Frame(self.gui.mainFrame)
        self.t1 = Label(self.mframe, text="起始数据")
        self.e11 = Entry(self.mframe)
        self.e11.insert(tk.INSERT, "output")
        self.e12 = Entry(self.mframe)
        self.e12.insert(tk.INSERT, "0")
        self.t2 = Label(
            self.mframe, text="数据输入列表/表达式")
        self.e22 = Entry(self.mframe)
        self.e22.insert(tk.INSERT, "range(10)")
        self.t23 = Label(self.mframe, text="输入数据变量名")
        self.e23 = Entry(self.mframe)
        self.e23.insert(tk.INSERT, "i")
        self.t3 = Label(self.mframe, text="迭代次数:")
        self.e3 = Entry(self.mframe)
        self.e3.insert(tk.INSERT, "auto")
        self.t4 = Label(self.mframe, text="输出变量")
        self.t41 = Entry(self.mframe)
        self.t41.insert(tk.INSERT, "output")
        self.t42 = Label(self.mframe, text="输出结果")
        self.t43 = Text(self.mframe, bg="white", relief="groove")
        self.t43.config(state="disabled")
        self.t6 = Label(self.mframe, text="单次迭代代码:")
        self.code_text = Text(self.mframe)
        self.code_text.insert(tk.INSERT, "output += i**2")
        self.run_button = Button(self.mframe, text="执行", command=self.run)
        self.chose = IntVar()
        self.save_chose = Checkbutton(
            self.mframe, text="是否保存", variable=self.chose)
        self.t7 = Text(self.mframe)
        self.t7.insert(
            tk.INSERT, "可从变量组导入数据,变量组名为 var_group , 格式为`var_group[group_name][var_name]`")
        self.t7.config(state="disabled")

    def run(self):
        scope = {}
        var_group = self.nb.var_group
        scope = {"var_group": {v: {
            i: var_group[v].vars[i].value for i in var_group[v].vars} for v in var_group}}
        scope[self.e11.get()] = eval(self.e12.get())  # 设置起始数据
        try:
            input_list = list(eval(self.e22.get(), scope))  # 输入数据列表
        except Exception as e:
            easygui.msgbox(f"输入数据列表/表达式异常:{e}")
            return 0
        times = int(self.e3.get()) if self.e3.get(
        ) != "auto" else len(input_list)  # 设置迭代次数
        name = self.e23.get()
        code = self.code_text.get("1.0", tk.END)  # 代码
        ts = datetime.datetime.now()
        for i in range(times):
            scope[name] = input_list[i]  # 设置输入数据
            try:
                exec(code, scope)
            except Exception as e:
                easygui.exceptionbox(e)
                break

        else:
            te = datetime.datetime.now()
            # 根据ts,te求运行消耗的时间
            runtime = (te-ts).total_seconds()
            self.t43.config(state="normal")
            self.t43.delete("1.0", tk.END)
            self.t43.insert(tk.INSERT, str(scope[self.t41.get()]))
            self.t43.config(state="disabled")
            output_msg = f"""
迭代执行完毕
起始数据:{scope[self.e11.get()]}
数据输入列表/表达式:{input_list}
迭代次数:{times}
输出变量:{self.t41.get()}
输出结果:{scope[self.t41.get()]}
运行时间:{runtime} //数据有一定误差
    """
            if self.chose.get() == 1:  # 当保存勾选时
                name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+"-iter-output"
                output = {"times": times,
                          "input_list": input_list,
                          "name": name,
                          "code": code,
                          "output": scope[self.t41.get()]
                          }
                self.nb.var_group_add(name, vars=output, path=[
                                      self.nb.save[0], name+".json"])
                self.nb.var_group[name].load_dict(self.nb.var_group[name].vars)
                output_msg += f"\n\n保存为 {name} 变量组\n保存至{os.path.abspath(self.nb.var_group[name].path)} 文件"

            easygui.msgbox(output_msg)

    def main(self):
        easygui.msgbox("此工具用于迭代执行代码\n本工具内所有代码,数据,表达式请使用 Python 编写")
        self.mframe.place(relwidth=1, relheight=1)
        self.t1.place(relx=0.02, rely=0.05, relwidth=0.1,
                      relheight=0.05, anchor="nw")
        self.e11.place(relx=0.12, rely=0.05, relwidth=0.1,
                       relheight=0.05, anchor="nw")
        self.e12.place(relx=0.12, rely=0.1, relwidth=0.1,
                       relheight=0.05, anchor="nw")

        self.t2.place(relx=0.02, rely=0.2, relwidth=0.12,
                      relheight=0.05, anchor="nw")
        self.e22.place(relx=0.12, rely=0.2, relwidth=0.1,
                       relheight=0.05, anchor="nw"
                       )
        self.t23.place(relx=0.02, rely=0.25, relwidth=0.1,
                       relheight=0.05, anchor="nw")
        self.e23.place(relx=0.12, rely=0.25, relwidth=0.1,
                       relheight=0.05, anchor="nw")
        self.t3.place(relx=0.02, rely=0.35, relwidth=0.1,
                      relheight=0.05, anchor="nw")
        self.e3.place(relx=0.12, rely=0.35, relwidth=0.1,
                      relheight=0.05, anchor="nw")

        self.t4.place(relx=0.02, rely=0.45, relwidth=0.1,
                      relheight=0.05, anchor="nw")
        self.t41.place(relx=0.12, rely=0.45, relwidth=0.1,
                       relheight=0.05, anchor="nw")
        self.t42.place(relx=0.02, rely=0.5, relwidth=0.1,
                       relheight=0.05, anchor="nw")
        self.t43.place(relx=0.12, rely=0.51, relwidth=0.1,
                       relheight=0.05, anchor="nw")

        self.t6.place(relx=0.22, rely=0.05, relwidth=0.1, relheight=0.05)
        self.code_text.place(relx=0.23, rely=0.1, relwidth=0.7, relheight=0.7)

        self.run_button.place(relx=0.52, rely=0.05,
                              relwidth=0.1, relheight=0.05)

        self.save_chose.place(relx=0.02, rely=0.55,
                              relwidth=0.1, relheight=0.05, anchor="nw")

        self.t7.place(relx=0.02, rely=0.6, relwidth=0.1, relheight=0.2)

    def quit(self):
        self.mframe.place_forget()


class VarCala:
    def __init__(self, nb):
        self.gui = nb
        self.nb = nb.notebook
        self.scope = {}
        self.mframe = Frame(self.gui.mainFrame)
        self.t11 = Label(self.mframe, text="选择变量组")
        self.c1 = ttk.Combobox(self.mframe)
        self.t12 = Label(self.mframe, text=f"组内变量: ")
        self.t13 = Text(self.mframe, relief="groove", state="disabled")
        self.c1.bind("<<ComboboxSelected>>", self.c1_chose)
        self.output_l = Label(self.mframe, text="计算结果: ")
        self.output_text = Text(self.mframe, bg="white", relief="groove")
        self.run_b = Button(self.mframe, text="计算", command=self.run)
        self.cala_code = Text(self.mframe, bg="white", relief="groove")
        self.output2t = Label(self.mframe, text="输出到变量:")
        self.output2e = Entry(self.mframe)

    def c1_chose(self, event):
        widget = event.widget
        get_val = widget.get()
        var_group = self.nb.var_group[get_val]
        self.scope = {v: var_group[v].value for v in var_group.vars}
        var_l = "\n".join(
            ":".join((i, str(self.scope[i]))) for i in self.scope)
        self.t13.config(state="normal")
        self.t13.delete("1.0", tk.END)
        self.t13.insert(tk.INSERT, var_l)
        self.t13.config(state="disabled")

    def run(self):
        code = self.cala_code.get("1.0", tk.END)
        output = eval(code, self.scope)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.INSERT, str(output))
        if self.output2e.get() != "":
            output2 = self.output2e.get()
            var_group = self.nb.var_group[self.c1.get()]
            if output2 not in var_group.vars:
                var_group.add(name=output2, value=output)
            else:
                var_group.vars[output2].value = output
            var_l = "\n".join(
                ":".join((i, str(var_group.vars[i].value))) for i in var_group.vars)
            self.t13.config(state="normal")
            self.t13.delete("1.0", tk.END)
            self.t13.insert(tk.INSERT, var_l)
            self.t13.config(state="disabled")

    def main(self):
        easygui.msgbox("此工具用于变量,可导入\n本工具内所有代码,数据,表达式请使用 Python 编写")
        self.mframe.place(relwidth=1, relheight=1)
        self.c1["values"] = tuple(self.nb.var_group.keys())
        self.t11.place(relx=0.019, rely=0.05, relwidth=0.1,
                       relheight=0.05, anchor="nw")
        self.c1.place(relx=0.12, rely=0.05, relwidth=0.1,
                      relheight=0.05, anchor="nw")
        self.t12.place(relx=0.04, rely=0.1, relwidth=0.05,
                       relheight=0.05, anchor="nw")
        self.t13.place(relx=0.04, rely=0.15, relwidth=0.2,
                       relheight=0.2, anchor="nw")
        self.run_b.place(relx=0.3, rely=0.05, relwidth=0.05,
                         relheight=0.05, anchor="nw")
        self.cala_code.place(relx=0.3, rely=0.1, relwidth=0.5,
                             relheight=0.3, anchor="nw")
        self.output_l.place(relx=0.05, rely=0.4, relwidth=0.1,
                            relheight=0.05, anchor="nw")
        self.output_text.place(relx=0.05, rely=0.45, relwidth=0.75,
                               relheight=0.3, anchor="nw")
        self.output2t.place(relx=0.05, rely=0.8, relwidth=0.1,
                            relheight=0.05, anchor="nw")
        self.output2e.place(relx=0.15, rely=0.8, relwidth=0.1,
                            relheight=0.05, anchor="nw"
                            )

    def quit(self):
        self.mframe.place_forget()
