import json
import os
import atexit


class Notebook:
    def __init__(self):
        self.text = ""  # 文本
        self.val_group = {}  # 变量组
        self.save = None

    def __str__(self):
        return f"NoteBook:(save:'{self.save}'"

    def __repr__(self):
        return self.__str__()

    def output_save(self):
        json.dump(os.path.join(
            self.save, "val_group.json"), self.val_group, indent=4, ensure_ascii=False)
        open(os.path.join(self.save, "text.txt")).write(self.text)

    def save_set(self, path):
        if os.path.exists(path):
            self.save = path
