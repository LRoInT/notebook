import tkinter
import notebook as nb



class NoteBookGUI:  # 窗口类
    def __init__(self, notebook: nb.Notebook):
        self.root = tkinter.Tk()
        self.root.title("快速笔记本")
        self.root.geometry("1000x600")
        self.notebook = notebook

    def __str__(self) -> str:
        return f"NoteBookGUI:(notebook:{self.notebook},size:{self.root.geometry()})"

    def __repr__(self) -> str:
        return self.__str__()
