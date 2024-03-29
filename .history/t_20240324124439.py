from main.book import NoteBook
n=NoteBook()
for p in ["mm.py"]:
    name="5555"
    test_l={}
    print(locals())
    exec(open(p).read(),test_l)
    print(test_l)
print(name)