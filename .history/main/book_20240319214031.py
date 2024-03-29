import json
import os
import atexit


class Notebook:
    def __init__(self):
        self.save = ""
        self.text = "" # 文本
        self.val_group = {}  # 变量组
        self.output=None

    def __str__(self):
        return f"NoteBook:(save:'{self.save}'"

    def __repr__(self):
        return self.__str__()
    def output_save(self):
        save_val=json.dump(os.path.join(path,"val_group.json"),self.val_group,indent=4,ensure_ascii=False)

    def output_self(self,path):
        if os.path.exists(path):
            self.output=path
    

