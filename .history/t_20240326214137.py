from main.book import NoteBook
n=NoteBook()
n.plugin_set("mm.py")
print(n.plugins)
print(n.plugins["mmm"][0].run())