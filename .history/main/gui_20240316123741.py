import tkinter
from tkinter import *
from main import *


class NoteBookGUI:  # 窗口类

    def __init__(self, notebook:book.Notebook):
        self.root = tkinter.Tk()
        self.root.title("快速笔记本")
        self.root.geometry("1000x600")
        self.mainFrame = Frame(self.root, width=800, height=500)
        self.notebook = notebook
        self.widget_dict={
            "page_option":[]
        }

    def __str__(self) -> str:
        return f"NoteBookGUI:(notebook:{self.notebook},size:{self.root.geometry()})"

    def __repr__(self) -> str:
        return self.__str__()
    
    def windows_init(self):
        for b in self.widget["page_option"]:
            pass
        self.mainFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
        self.root.mainloop()
    def run(self):
        pass