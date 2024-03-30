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
        t1=tkinter.Label(self.nb.root,text="hello world in nb.test")