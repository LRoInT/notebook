import json
import os
import atexit
import numpy as np
import re

get_word=re.compile("[a-zA-Z]")#获取字母
wordintext=lambda t:"".join(get_word.findall(t)).lower()
get_num=re.compile("[0-9]") #获取数字
numintext=lambda t:int("".join(get_num.findall(t)))
def title2num(text):
        words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        text=wordintext(text)
        ct = text[::-1]
        if len(text) == 1:
            return words.find(text)
        else:
            num = 0
            for i in range(len(text)):
                num += 26**i*(words.find(ct[i])+1)

        return num

class form_cell:  # 单元格类
    def __init__(self, data, type="int"):
        self.data = data
        self.type = type


class form2d:  # 表格类
    def __init__(self, object=[[]]) -> None:
        for i in object:
            for j in i:
                if isinstance(j, (list, tuple)):
                    raise TypeError("Nested lists are not allowed in tables")
                j = form_cell(j)
        self.form = np.array(object)

    def __getitem__(self, index):
        print(index)
        if type(index)==str:
            column=title2num(index)
            line=numintext(index)
            print(line,column)

        


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
            atexit.register(self.output_save)  # 开启自动保存
            return True
        else:
            return False
