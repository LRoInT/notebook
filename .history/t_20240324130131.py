from main.book import NoteBook
scope={} #设置作用域
exec(open("mm.py", encoding="utf-8").read(),scope)
print(scope.keys())
n=NoteBook()
n.plugin_set("mm.py")
print(n.plugins)