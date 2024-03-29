from main.book import NoteBook
n=NoteBook()
n.plugin_set("mm.py")
tp=n.plugin["mmm"]
tp.run()