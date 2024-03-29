import tkinter as tk
root=tk.Tk()
root.geometry("200x200")
a=tk.Button(root,text="hello")
b=tk.Frame(bg="red",width=100,height=100,bd=5)
b.place(relx=0.5,rely=0.5,anchor="sw")
a.master=b
a.pack()
a.mainloop()
