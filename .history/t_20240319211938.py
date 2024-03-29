import tkinter as tk
# 创建一个窗口
root = tk.Tk()

# 创建一个框架
frame1 = tk.Frame(root)
frame1.pack()

# 创建一个按钮，并将它添加到frame1中
button = tk.Button(frame1, text="这是一个按钮")
button.pack()

# 将按钮从frame1中移除，并将其添加到frame2中
button.master = frame2 = tk.Frame(root)
frame2.pack()

# 运行主循环
root.mainloop()
