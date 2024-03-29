import os
import sys
import getopt
import json

argv_list = getopt.getopt(sys.argv[1:], "h:o:p:", [
                          "--history=", "--output=", "--pulgin="])[0]  # 参数列表
argv = {"history": None,  # 参数字典
        "output": None,
        "pulgin": None}

for i in argv_list:  # 填写参数字典
    if i[0] == '-h' or i[0] == '--history':
        argv['history'] = i[1]
    elif i[0] == '-o' or i[0] == '--output':
        argv['output'] = i[1]
    elif i[0] == '-p' or i[0] == '--pulgin':
        argv['pulgin'] = i[1]


class Notebook:
    def __init__(self, argv):
        self.history = []
        self.output = lambda x: print(x)
        self.pulgin = {}
        self.cmdlist = {"exit": "sys.exit()"}
        self.argv = argv

    def get_history(self):  # 获取历史
        argv = self.argv
        if argv['history'] == None:
            return None
        else:
            if os.path.exists(argv['history']):
                self.history = json.load(open(argv['history']))
                return None

    def get_output(self):
        argv = self.argv
        if argv['output'] == None:
            return None
        else:
            if os.path.exists(argv['output']):
                def output_fun(x):
                    print(x)
                    self.history.append(x)
                self.output = output_fun
                return None

    def setting(self):
        self.get_history()
        self.get_output()

    def get_output(self, x):
        if x.startswith('!'):
            return eval(x[1:])
        elif x.startswith('@'):
            if x[1:] in self.cmdlist:
                exec(self.cmdlist[x[1:]])
                return None
            elif x[1:].startswith('[file]'):
                exec(open(x[1:]).read())
                return None

    def run(self):
        while True:
            input_t = input(">>>")
            output_t = self.output(input_t)
            if output_t == None:
                continue
            print("\r")
            self.


if __name__ == '__main__':
    pass
