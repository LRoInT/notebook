import notebook as nb
import tkinter
import easygui as eg

notebook=nb.Notebook()
root=tkinter.Tk()

config_list=["加载历史文件","记录保存位置","加载插件文件"]
use_config=eg.multenterebox(msg="请输入配置",title="输入配置",choices=config_list)
print(use_config)