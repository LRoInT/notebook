from main.book import NoteBook
n=NoteBook()
for p in ["mm.py"]:
    print(locals())
    exec(open(p).read())
    print(name,locals())
print(name)