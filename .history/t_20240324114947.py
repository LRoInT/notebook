import tkinter as tk
from tkinter import ttk

def on_save():
    print("保存:", entry.get())

root = tk.Tk()
root.title("树视图与输入框")

treeview = ttk.Treeview(root, columns=("姓名", "年龄"), show="headings")
treeview.heading("姓名", text="姓名")
treeview.heading("年龄", text="年龄")

entry = ttk.Entry(root)
entry.pack()

button = ttk.Button(root, text="保存", command=on_save)
button.pack()

treeview.pack(fill=tk.BOTH, expand=True)

root.mainloop()

