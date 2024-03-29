
import easygui as eg
from main import *


notebook = book.Notebook()
nbgui = gui.NoteBookGUI(notebook)

config_list = ["加载历史文件", "记录保存位置", "加载插件文件"]
use_config: list
nbgui.run()