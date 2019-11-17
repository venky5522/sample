class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def hello(self):
        print("in hello method")
        c = self.a * self.b
        print(c)
class B(A):
    def __init__(self,c):
        A.__init__(self,10,20)
        self.c = c
    def welcome(self):
        print(self.a,self.b,self.c)
obj = B(40)
obj.welcome()
obj.hello()