from proglib import *
b = book.NoteBook()


class c:
    def __init__(self, value):
        self.value = value+777


b.json2obj.update({"c": lambda x: c(x["value"])})
b.obj2json.update({c: lambda x: {"__class__": "c", "value": x.value}})
print(b.json2obj)
b.note_set("./tdir")
print(b.var_group["b"]["333"].value.value)
b.output_save("./ttdir")
