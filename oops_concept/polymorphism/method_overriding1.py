class x:
    def m1(self):
        print("in no parm of x")
class y(x):
    def m1(self):
        print("in one arm of y")
y1 = y()
y1.m1()
x1 = x()
x1.m1()