class x:
    def __init__(self):
        self.a = 100
        self.b = 200
class y(x):
    def __init__(self):
        super().__init__()
        self.c = 300
        self.d = 400
y1 = y()
print(y1.a)
print(y1.b)
print(y1.c)
print(y1.d)
x1 = x()
print(x1.a)
print(x1.b)

