import easygui
import tkinter

a="22234"
class test1Run:
    def __init__(self,nb):
        self.gui=nb
        self.nb=nb.notebook
    
    def main(self):
        self.nb.text=a
        print(self.nb.text)
        easygui.msgbox(msg="hello world in nb.test",title="hello")
        self.t1=tkinter.Label(self.gui.mainFrame,text=f"text{self.nb.text} in nb.test")
        self.t1.place(relx=0.15, rely=0.85)
    
    def quit(self):
        print("quit")
        self.t1.place_forget()