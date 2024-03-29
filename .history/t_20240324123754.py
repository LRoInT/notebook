from main.book import NoteBook
n=NoteBook()
name="6666"
for p in ["mm.py"]:
    print(locals(),globals())
    exec(open(p).read())
    print(name,locals(),globals())
print(name)