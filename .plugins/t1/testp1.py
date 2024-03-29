import easygui
class test1Run:
    def __init__(self,nb):
        self.nb=nb
    
    def main(self):
        self.nb.text="hello world"
        print(self.nb.text)
        easygui.msgbox(msg="hello world in nb.test",title="hello")
        