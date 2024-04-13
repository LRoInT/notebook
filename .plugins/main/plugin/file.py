import os
import easygui


class file_manager:
    def __init__(self, nb):
        self.gui = nb
        self.nb = nb.notebook

    def _load(self, path):
        self.nb.plugin_quit()
        try:
            self.nb.note_set(path)
        except Exception as e:
            easygui.msgbox(f"错误:{e}", title="加载错误")
        self.nb.lib["mainlib"].NBWelcome(self.gui)
        self.gui.root.update()

    def load_dir(self):
        path = easygui.diropenbox(title="选择文件夹")
        if path is None:
            return 0
        if os.path.exists(path):
            if bool(self.nb.text) or bool(self.nb.var_group):
                chose = easygui.ccbox(
                    "加载文件将会清空当前内容\n是否加载", choices=["加载", "取消"], title="警告")
                if chose:
                    self._load(path)
            else:
                self._load(path)
        else:
            easygui.msgbox("文件不存在", "错误")

    def load_file(self):
        path = easygui.fileopenbox(title="选择文件")
        if path is None:
            return 0
        if os.path.exists(path):
            if bool(self.nb.text) or bool(self.nb.var_group):
                chose = easygui.ccbox(
                    "加载文件将会清空当前内容\n是否加载", choices=["加载", "取消"], title="警告")
                if chose:
                    self._load(path)
            else:
                self._load(path)
        else:
            easygui.msgbox("文件不存在", "错误")

    def save_as_file(self):
        path = easygui.filesavebox(title="选择文件", filetypes=[
                                   [".json", "JSON 文件"]])
        if path is None:
            return 0
        try:
            self.nb.output_save(path, type="file")
        except Exception as e:
            easygui.msgbox(f"错误:{e}", title="保存错误")

    def save_as_dir(self):
        path = easygui.diropenbox(title="选择文件夹")
        if path is None:
            return 0
        try:
            self.nb.output_save(path, type="dir")
        except Exception as e:
            easygui.msgbox(f"错误:{e}", title="保存错误")

    def save(self):
        if self.nb.save is not None:
            self.nb.output_save()
        else:
            self.save_as()
