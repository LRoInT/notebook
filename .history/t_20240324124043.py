from main.book import NoteBook
n=NoteBook()
for p in ["mm.py"]:
    name="5555"
    print(locals())
    exec(open(p).read())
    print(name,locals())
print(name)