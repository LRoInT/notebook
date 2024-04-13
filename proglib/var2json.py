import json
# 变量编编码为 JSON 字符串

# 解码器


def check(func):
    def wrapper(obj_convert, *args, **kwarg):
        print(func.__name__)
        print(args, kwarg)
        out = func(obj_convert)
        print(out, "\n---")
        return out
    return wrapper


def NBJsonDecoder(obj_convert):  # JSON解码器
    # obj_conver: {class_name: func}
    # class_name: "__class__" 内的值
    # func: 解码函数
    def object_hook(obj):
        if "__class__" in obj:
            try:
                return obj_convert[obj["__class__"]](obj)  # 解码
            except:
                return obj
        return obj
    return object_hook


def NBJsonEncoder(obj_convert):  # JSON编码器
    # obj_conver: {obj_class: func}
    # obj_class: 处理对象的类名
    # func: 编码函数
    def encode(obj):
        if type(obj) in obj_convert:
            return obj_convert[type(obj)](obj)
        else:
            json.JSONEncoder.encode(obj)
    return encode
