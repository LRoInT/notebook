import main as nb
import tkinter
import easygui as eg


class NoteBookGUI:
    def __init__(self, notebook: nb.Notebook):
        self.root = tkinter.Tk()
        self.notebook = notebook
    
    def __str__(self) -> str:
        return f"NoteBookGUI:(notebook:{self.notebook},size:{self.root.geometry()})"


notebook = nb.Notebook()
nbgui=NoteBookGUI(notebook)

config_list = ["加载历史文件", "记录保存位置", "加载插件文件"]
use_config: list
use_config = eg.multenterbox(
    msg="请输入配置", title="输入配置", fields=config_list)  # type: ignore
notebook.load(save=use_config[0], load=use_config[1], plugin=use_config[2])
print()
