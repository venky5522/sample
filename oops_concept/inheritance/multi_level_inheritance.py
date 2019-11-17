class x:
    def m1(self):
        print("in m1 method")
class y(x):
    def m2(self):
        print("in m2 method")
y1 = y()
y1.m1()
y1.m2()