import os
import easygui


class file_manager:
    def __init__(self, nb):
        self.gui = nb
        self.nb = nb.notebook

    def _load_file(self, path):
        self.nb.plugin_quit()
        self.nb.history_set(path)
        self.nb.lib["mainlib"].NBWelcome(self.gui)

    def load(self):
        path = easygui.diropenbox(title="选择文件夹")
        if os.path.exists(path):
            if bool(self.nb.text) or bool(self.nb.val_group):
                chose = easygui.ccbox(
                    "加载文件将会清空当前内容\n是否加载", choices=["加载", "取消"], title="警告")
                if chose:
                    self._load_file(path)
            else:
                self._load_file(path)
        else:
            easygui.msgbox("文件不存在", "错误")

    def save_as(self):
        path = easygui.diropenbox(title="选择文件夹")
        try:
            self.nb.output_save(path)
        except Exception as e:
            easygui.msgbox(f"错误:{e}",title="保存错误")

    def save(self):
        if self.nb.save is not None:
            self.nb.output_save()
        else:
            self.save_as()

    