class x:
    def m1(self):
        print("in m1 method")
class y(x):
    def m2(self):
        print("in m2 method")
class z(x):
    def m3(self):
        print("in m3 method")
y1 = y()
y1.m1()
y1.m2()
z1 = z()
z1.m1()
z1.m3()