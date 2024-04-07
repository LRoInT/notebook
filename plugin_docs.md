# PLUGIN 相关文档

插件为程序功能实现的方式

## 结构

> 本程序默认的插件目录为`.plugins`
>
>当一个目录中包含多个插件目录是,程序会遍历此目录
>
>一个直接含义插件的目录中应有一个`plugin.json`文件

```JSON
{
    "name": "ExamplePlugin",
    "mainFile":"main.py",
    "type": "..."
    ...
}
```

- `name`:插件名
- `mainFile`:插件主文件
- `type`:插件类型

## 功能型插件

> *该类型插件为默认类型*
> 功能型插件的`plugin.json`文件格式如下

```JSON
{
    "name": "ExamplePlugin",
    "mainFile":"main.py",
    "type":"plugin"
    ...
}
```

- `name`:见`结构`
- `mainFile`:见`结构`
- `"type":"plugin"`:声明插件为一个`功能型插件`,可省略

> 一个插件运行文件应为一个`Python`文件,有一个`[PluginName]Run`类

- `__init__`函数应包含一个`notebook`参数,该参数为`proglib.gui.NoteBookGUI`类的一个实例,有关`NoteBookGUI`类请参考[README.md](./README.md)
- `main`:作为插件的执行程序,不应包含参数
- `quit`:作为插件的退出程序,不应包含参数

``` Python
class PluginNameRun:
    # Code Here
    def __init__(self,notebook):
        self.gui=nb
        self.nb=nb.notebook
        # Code Here
    def main(self):
        # Code Here
    def quit(self):
        # Code Here
```

> 当插件中有`__other__`列表时,会将`__other__`中出现的其他信息添加

``` Python
name="Example"
__other__=["Example1","Example2"]
Example1="Example1"
Example2="Example2"
class ExampleRun:
    # Code Here
    def __init__(self,notebook):
        self.gui=nb
        self.nb=nb.notebook
        # Code Here
    def main(self):
        # Code Here
    def quit(self):
        # Code Here
```

> `NoteBookGUI`类中提供将插件加载带菜单栏中的函数`NoteBookGUI.plugin2menu`
> 该函数的参数为`(name,pluginclasa)`,`name`为插件的名称,`pluginclasa`为插件的运行类`(self)`

```Python
class ExampleRun:
    # Code Here
    def __init__(self,notebook):
        self.gui=nb
        self.nb=nb.notebook
        self.gui.plugin2menu("PluginName",self)
        # Code Here
    def main(self):
        # Code Here
    def quit(self):
        # Code Here
```

## 支持库

> *支持库加载时间早于插件*
> 支持库应为一个文件夹, 应包含一个`plugin.json`,格式如下

```JSON
{
    "name":"ExampleLib",
    "type":"lib",
    "key":"examplelib",
    "mainFile":"package_file"
}
```

- `name`:插件名
- `mainFile`:运行库文件,可为文件或文件夹
- `"type":"pluginlib"`:声明此插件为支持库
- `key`:支持库的键名,可省略,省略时为`name`

>当支持库被加载时,库内的属性会被加载到`NoteBook.lib[key]`下
---
>例:
>
> `el/plugin.json`

```JSON
{
    "name":"ExampleLib",
    "type":"lib",
    "key":"examplelib",
    "mainFile":"examplelib.py"
}
```

>
>`el/examplelib.py`

```Python
def func():
    print("NoteBook example")
```

> 程序:

``` Python
nb=proglib.book.NoteBook()
print("NoteBook Lib:"nb.lib)
"""
NoteBook Lib:{}
"""
nb.plugin_set("./el")
print("NoteBook Lib":nb.lib)
"""
NoteBook Lib:{'examplelib': {'func': <function func at 0x000001BAC7EC3E20>}}
"""
```

在以上示例中, 使用了`NoteBook.plugin_set`函数加载`el`支持库.加载后,`el/examplelib.py`中的`func`函数被加载到了`NoteBook.lib[examplelib]`中
