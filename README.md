# 快速笔记本

- 主程序: `program.py`

- 库:`main.py`

> 本程序使用`tkinter`及`easygui`库作为界面程序. 设计中将使用插件设计, 通过加载一个默认文件夹和可选文件夹内的插件使用.

## 库

- `book.py`: `Notebook`类及其他

- `gui.py`: `NoteBookGUI`类,页面库

---

### Book 部分
>
>`Notebook`类: 笔记本类,程序主要部分
>
#### Form
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

### GUI 部分
>
>![Windows](./gui.png)
>
>`NoteBookGUI.optionFrame`:选项栏
>
>`NoteBookGUI.mainFrame`:主页面
