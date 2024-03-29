import os
import sys
import json

class Notebook:
    def __init__(self):
        self.save=""
        self.pulgin=[]
        self.history=[]
    
    def __str__(self):
        return f"NoteBook:(save:{self.save},plugin:{self.pulgin},history:{self.history})"
    def __repr__(self):
        return self.__str__()
    def load(self,**argv):
        if argv["save"]!="":
            self.save=argv["save"]
        if argv["load"]!="":
            if os.path.exists(argv["load"]):
                load_history=json.load(open(argv["load"],encoding="utf-8"))
            else:
                print("文件不存在")
        if argv["plugin"]!="":
            self.pulgin.append(argv["plugin"])

        