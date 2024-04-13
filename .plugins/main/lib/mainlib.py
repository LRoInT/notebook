import tkinter as tk

lib=None

class NBWelcome:
    def __init__(self,nb):
        self.gui=nb
        self.nb=self.gui.notebook
        self.widgets:list[tuple]=[]
        text1=tk.Label(nb.mainFrame,text="欢迎使用多功能笔记本1.0",height=10,width=50)
        self.nb.inuse=self
        self.text1=text1
    
    def quit(self):
        self.text1.destroy()
