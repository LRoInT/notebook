import notebook as nb
import tkinter
import easygui as eg

notebook=nb.Notebook()
root=tkinter.Tk()
root.geometry("800x600")

config_list=["加载历史文件","记录保存位置","加载插件文件"]
use_config=eg.multenterbox(msg="请输入配置",title="输入配置",fields=config_list)
print(use_config)
notebook.load(save=use_config[0],load=use_config[1],plugin=use_config[2])

