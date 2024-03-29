import json
import os
import atexit
import numpy as np

class form2d: #表格,类似excel
    def __init__(self,object=[[]]) -> None:
        


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

    def save_set(self, path):  # 保存设置
        if path == "":  # 不保存
            self.save = None
            try:
                atexit.unregister(self.output_save)
            except:
                pass
            return True
        if os.path.exists(path):  # 检查路径是否存在
            self.save = path
            atexit.register(self.output_save)  # 关闭自动保存
            return True
        else:
            return False
