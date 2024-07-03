import tkinter as tk

lib=None

class NBWelcome:
    def __init__(self,nb):
        self.gui=nb
        self.nb=self.gui.notebook
        text1=tk.Label(nb.mainFrame,text="欢迎使用 多功能笔记本1.0",height=10,width=50)
        text1.pack()
        self.nb.inuse=self
        self.text1=text1
    
    def quit(self):
        self.text1.destroy()
    
class plugin_manager:
    def __init__(self,nb):
        self.gui=nb
        self.nb=nb.notebook
        self.plugin_load=self.nb.plugin_load