# 快速笔记本

- 主程序: `program.py`

- 库:`proglib.py`

- `.config.json`和`.page`:程序配置文件和页面文件夹

> 本程序使用`tkinter`及`easygui`库作为界面程序. 设计中将使用插件设计, 通过加载一个默认文件夹和可选文件夹内的插件使用.

## 库

- [`book.py`](./proglib/book.py): `Notebook`类及其他

- [`gui.py`](./proglib/gui.py): `NoteBookGUI`类,页面库

---

### [Book 部分](./proglib/book.py)

#### `Notebook`类

>笔记本类,程序主要部分
>
> `NoteBook.text`:笔记本文字内容,可作为插件的作用域
>
> `NoteBook.val_group`:笔记本的变量组,可作为插件的作用域
>
>`NoteBook.save`:保存路径
>
>`NoteBook.plugins`:笔记本插件字典,格式为`PluginName:[PluginClass,...]`
>
>`NoteBook.output_save`:笔记本内容输出函数
>
>`NoteBook.history_set`:历史加载函数
>
>`NoteBook.save_set`:输出设置
>
>`NoteBook.plugin_set`:插件设置

#### Form
>
> **此部分已废弃**
>
> **保存于 [`proglib.form`](./proglib/form.py)**
>
>`form_cell`类: 单元格类, 用于存储内容
>
> - `form_cell.data`: 单元格数据
> - `form_cell.style`: 单元格样式
> - `form_cell.type`: 单元格类型
>
>`form2d`类: 二维表类, 用于存储表
>
> - `form2d.form`类:一个 `np.array` 数组,数组中的每一项都应为一个`form_cell`类
>
---

### [GUI 部分](./proglib/book.py)

>![Windows](./gui.png)
>
#### `NoteBookGUI`类

> 程序主窗口类
>
> `NoteBookGUI.notebook`:一个`NoteBook`对象
>
>`NoteBookGUI.root`:一个`tkinter.Tk`对象,作为主窗口
>
>`NoteBookGUI.defaultconfig`:程序默认配置
>
>`NoteBookGUI.config`:程序当前配置
>
> `NoteBookGUI.option_menu`:菜单栏
>
> `NoteBookGUI.proglibFrame`:主页面
>
>`NoteBookGUI.config_set`:设置配置
>
>`NoteBookGUI.config_input`:检查配置正确并输入
>
>`NoteBookGUI.menu_init`:初始化菜单栏
>
>`NoteBookGUI.windows_init`:初始化窗口
>
>`NoteBookGUI.run`:运行 GUI 窗口

#### [Page_Load](./proglib/gui/page_load.py)

页面加载模块, 见 [page_docs.md](./page_docs.md)

### 插件部分

插件为程序功能实现的方式,见 [plugin_docs.md](./plugin_docs.md)
