import json
import os


class Notebook:
    def __init__(self):
        self.save = ""
        self.text = ""
        self.val_group = {}  # 变量组

    def __str__(self):
        return f"NoteBook:(save:'{self.save}'"

    def __repr__(self):
        return self.__str__()
