import tkinter as tk
root=tk.Tk()
root.geometry("200x200")

b=tk.Frame(width=100,height=100,bd=10,relief="groove")
b.place(relx=0.5,rely=0.5,anchor="nw")
a=tk.Button(text="hello")
a.master=b
a.pack()
a.mainloop()
