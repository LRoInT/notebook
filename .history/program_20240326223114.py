from main import *
notebook=book.NoteBook()
bookgui=gui.NoteBookGUI(notebook)
bookgui.config["plugins"][0]="./.plugins"
bookgui.run()