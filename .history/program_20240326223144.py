from main import *
notebook=book.NoteBook()
bookgui=gui.NoteBookGUI(notebook)
bookgui.config["plugins"].append("/.plugins")
bookgui.run()