# NOTE SAVE 文档

本文档主要讲述关于笔记保存的格式

## 单文件

>当保存为文件时,应保存为一个JSON文件,格式如下

```JSON
{
    "text":{
        "text_name":"text"
    },
    "var":{
        "var_name":"var_value"
    }
}
```

- `text`: 文本内容字典
- `var`: 变量内容字典

## 文件夹

>当保存为文件夹时,应包含为一个`note.json`文件,格式如下

```JSON
{
    "text":{
        "text_name":"text_file_path"
    },
    "var":{
        "var_name":"var_file_path
    }
}
```

- `text`: 文本文件路径字典
- `var`: 变量文件路径字典
