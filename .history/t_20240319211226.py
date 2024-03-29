import tkinter as tk
root=tk.Tk()
root.geometry("200x200")
a=tk.Button(root,text="hello")
b=tk.Frame(bg="red",width=100,height=100)
a.master=root
a.pack()
a.mainloop()
