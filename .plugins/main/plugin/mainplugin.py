from editon import *
from file import *


class mainpluginRun:
    def __init__(self, nb):
        self.gui = nb
        self.nb = nb.notebook
        self.te = NBTextEditon(self.gui)
        self.gui.plugin2menu("文本编辑器", self.te, self.gui.plugins_menu)
        self.ve = NBValEditon(self.gui)
        self.gui.plugin2menu("变量编辑器", self.ve, self.gui.plugins_menu)
        fl = file_manager(self.gui)
        # self.gui.file_menu.add_command(label="加载文件", command=fl.load_file)
        self.gui.file_menu.add_command(label="加载", command=fl.load_dir)
        # self.gui.file_menu.add_command(label="另存为文件", command=fl.save_as_file)
        self.gui.file_menu.add_command(label="另存为", command=fl.save_as_dir)
        self.gui.file_menu.add_command(label="保存", command=fl.save)
