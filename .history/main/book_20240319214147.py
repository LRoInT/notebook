import json
import os
import atexit


class Notebook:
    def __init__(self):
        self.save = ""
        self.text = ""  # 文本
        self.val_group = {}  # 变量组
        self.output = None

    def __str__(self):
        return f"NoteBook:(save:'{self.save}'"

    def __repr__(self):
        return self.__str__()

    def output_save(self):
        json.dump(os.path.join(
            self.output, "val_group.json"), self.val_group, indent=4, ensure_ascii=False)
        open(os.path.join(self.output, "text.txt")).write(self.text)


    def output_set(self, path):
        if os.path.exists(path):
            self.output = path
