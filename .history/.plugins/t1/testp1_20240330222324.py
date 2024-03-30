import easygui
import tkinter
class test1Run:
    def __init__(self,nb):
        self.gui=nb
        self.nb=nb.notebook
    
    def main(self):
        self.nb.text="hello world"
        print(self.nb.text)
        easygui.msgbox(msg="hello world in nb.test",title="hello")
        t1=tkinter.Label(self.gui.mainFrame,text=f"text{self.nb.text} in nb.test")
        t1.place(relx=0.15, rely=0.85)