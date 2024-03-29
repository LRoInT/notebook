import tkinter
from tkinter import *
import main as nb


class NoteBookGUI:  # 窗口类

    def __init__(self, notebook:nb.Notebook):
        self.root = tkinter.Tk()
        self.root.title("快速笔记本")
        self.root.geometry("1000x600")
        self.mainFrame = Frame(self.root, width=800, height=500)
        self.notebook = notebook

    def __str__(self) -> str:
        return f"NoteBookGUI:(notebook:{self.notebook},size:{self.root.geometry()})"

    def __repr__(self) -> str:
        return self.__str__()

    def run(self):
        self.mainFrame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
