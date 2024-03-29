class t1:
    def __init__(self,v):
        self.v=v
    def __getitem__(self,item):
        print(item)

a=t1(4)
a["a":"b"]