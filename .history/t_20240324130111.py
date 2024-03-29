from main.book import NoteBook
scope={} #设置作用域
exec(open("mm.py", encoding="utf-8").read(),scope)
print(scope.keys())
n=NoteBook()
print(n.plugins)