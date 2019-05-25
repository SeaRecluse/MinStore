class A:
    key1=1
    def __init__(self):
        self.key2=2
a = A()
b = a
dic = {'cls':b}
print(dic['cls'].key1,dic['cls'].key2)
a.key1,a.key2 = 3,4
print(dic['cls'].key1,dic['cls'].key2)