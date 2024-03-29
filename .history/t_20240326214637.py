from main.book import NoteBook
n=NoteBook()
n.plugin_set(".plugins")
print(n.plugins)
print(n.plugins["mmm"][0].run())