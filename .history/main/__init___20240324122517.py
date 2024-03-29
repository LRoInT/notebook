import os
import json
import easygui as eg
import main.book
import main.gui
__all__ = ["book", "gui"]

def load_config(path,notebook:main.book.NoteBook):
    config=json.load(open(path,"r",encoding="utf-8"))
    
