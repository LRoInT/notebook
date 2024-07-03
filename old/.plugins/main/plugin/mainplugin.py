
from editon import *
from file import *
from tool import *
from config import *


class NBWelcome:
    def __init__(self, nb):
        self.gui = nb
        self.nb = self.gui.notebook
        self.widgets: list[tuple] = []
        text1 = tk.Label(nb.mainFrame, text="欢迎使用多功能笔记本1.0", font=("微软雅黑", 20))

        self.widgets: list[tuple | list] = [
            [text1, {"relx": 0.0, "rely": 0.025, "relwidth": 0.5, "relheight": 0.2}]]

    def main(self):
        self.nb.plugin_quit()
        self.nb.inuse = self
        for w in self.widgets:
            w[0].place(**w[1])

    def quit(self):
        for w in self.widgets:
            w[0].place_forget()


def rmdir(path):
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            os.remove(os.path.join(path, f))
        elif os.path.isdir(os.path.join(path, f)):
            rmdir(os.path.join(path, f))
    os.rmdir(path)


def del_temp():
    rmdir(".nb_temp")


class mainpluginRun:
    def __init__(self, nb):
        self.gui = nb
        self.nb = nb.notebook
        self.te = NBTextEditon(self.gui)
        self.gui.plugin2menu("文本编辑器", self.te, self.gui.plugins_menu)
        self.ve = NBValEditon(self.gui)
        self.gui.plugin2menu("变量编辑器", self.ve, self.gui.plugins_menu)
        self.fl = file_manager(self.gui)
        self.gui.file_menu.add_command(label="新建", command=self.new)
        # self.gui.file_menu.add_command(label="加载文件", command=fl.load_file)
        self.gui.file_menu.add_command(label="加载", command=self.open)
        # self.gui.file_menu.add_command(label="另存为文件", command=fl.save_as_file)
        self.gui.file_menu.add_command(
            label="另存为", command=self.fl.save_as_dir)
        self.gui.file_menu.add_command(label="保存", command=self.fl.save)
        self.cala=VarCala(self.gui)
        self.gui.plugin2menu("变量计算工具", self.cala, self.gui.plugins_menu)
        self.it = iterateTool(self.gui)
        self.gui.plugin2menu("迭代执行工具", self.it, self.gui.plugins_menu)
        self.pl = plugin_loader(self.gui)
        self.gui.config_menu.add_command(label="加载插件", command=self.pl.main)
        self.gui.config_menu.add_command(
            label="已加载插件", command=self.pl.loaded_func)
        # 设置临时目录
        if not os.path.exists(".nb_temp"):
            os.makedirs("./.nb_temp")
        self.nb.save = ["./.nb_temp", "dir"]

        # ---
        self.set_welcome()

    def new(self):
        if self.fl.new()==0:
            return 0
        self.welcome.widgets[3][0].config(text="当前加载文件夹：" + self.nb.save[0])
        self.gui.root.title(self.gui.root.title() + " - " + self.nb.save[0])
        self.welcome.main()

    def open(self):
        if self.fl.load_dir()==0:
            return 0
        self.welcome.widgets[3][0].config(text="当前加载文件夹：" + self.nb.save[0])
        self.gui.root.title(self.gui.root.title() + " - " + self.nb.save[0])
        self.welcome.main()


    def set_welcome(self):
        widgets = [
            [Button(self.gui.mainFrame, text="加载", command=self.open), {
                "relx": 0.05, "rely": 0.25, "relwidth": 0.07, "relheight": 0.1, "anchor": "nw"}],
            [Button(self.gui.mainFrame, text="新建", command=self.new), {
                "relx": 0.05, "rely": 0.4, "relwidth": 0.07, "relheight": 0.1, "anchor": "nw"
            }],
            [Label(self.gui.mainFrame, text="当前加载文件夹：无", font=("微软雅黑", 10)), {
                "relx": 0.15, "rely": 0.2, "relwidth": 0.2, "relheight": 0.1, "anchor": "nw"
            }]

        ]
        self.welcome = NBWelcome(self.gui)  # 欢迎页面
        self.welcome.widgets.extend(widgets)
        self.welcome.main()
