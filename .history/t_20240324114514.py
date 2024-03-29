import tkinter as tk
from tkinter import ttk

# 创建主窗口
root = tk.Tk()
root.title("表格示例")

# 创建一个表格
table = ttk.Treeview(root, columns=("姓名", "年龄", "城市"), show="headings")
table.heading("姓名", text="姓名")
table.heading("年龄", text="年龄")
table.heading("城市", text="城市")

# 添加一些数据
data = [
    ("张三", 25, "北京"),
    ("李四", 30, "上海"),
    ("王五", 22, "广州"),
    ("赵六", 28, "深圳"),
]

for item in data:
    table.insert("", "end", values=item)

# 将表格添加到主窗口
table.pack(fill=tk.BOTH, expand=True)

# 运行主循环
root.mainloop()
