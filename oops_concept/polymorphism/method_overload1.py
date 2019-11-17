class x:
    def m1(self):
        print("in one parm of x")
    def m1(self,a):
        print("in two parm of x")
    def m1(self,a,b):
        print("in three parm of x")
x1 = x()
x1.m1(10,20)