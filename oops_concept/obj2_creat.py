class welcome:
    a = 100
    b = 200
    def __init__(self,m,n):
        self.m = m
        self.n = n
    def hello(self):
        if self.m > self.n:
            return (self.a+self.b)*self.m
        else:
            return (self.a-self.b)*self.n
obj = welcome(30,20)
val = obj.hello()
print(val)