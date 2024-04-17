import easygui


class plugin_loader:
    def __init__(self, nb):
        self.gui = nb
        self.nb = nb.notebook

    def main(self):
        path = easygui.diropenbox("选择插件文件夹")
        self.nb.plugin_set(path, run=self.gui)
    
    def loaded_func(self):
        easygui.msgbox(f"已加载插件:\n{self.nb.plugin_loaded()}")