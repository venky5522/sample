class opoverload:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return "operator overload"
    def __add__(self, c):
        x = self.a+c.a
        y = self.b+c.b
        return x+y
    def __sub__(self,d):
        x = self.a-d.a
        y = self.b-d.b
        return x-y
obj=opoverload(10,20)
obj1=opoverload(30,40)
val =obj+obj1
print(val)
#obj.__str__()
print(obj)