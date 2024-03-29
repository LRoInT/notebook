import os
import sys
import getopt
import json

argv_list = getopt.getopt(sys.argv[1:], "h:o:p:", [
                          "--history=", "--output=", "--pulgin="])[0] #参数列表
argv = {"history": None,  #参数字典
        "output":None,
        "pulgin":None}

for i in argv_list: #填写参数字典
    if i[0] == '-h' or i[0] == '--history':
        argv['history'] = i[1]
    elif i[0] == '-o' or i[0] == '--output':
        argv['output'] = i[1]
    elif i[0] == '-p' or i[0] == '--pulgin':
        argv['pulgin'] = i[1]


def get_history(): #获取历史
    if argv['history'] == None:
        return [],None
    else:
        if os.path.exists(argv['history']):
            history=json.load(open(argv['history']))
            return history,argv['history']


def main():
    pass


if __name__ == '__main__':
    history, history_path = get_history()
    main()
