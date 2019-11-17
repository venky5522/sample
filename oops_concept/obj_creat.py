class hello:
    a = 10
    b = 20
    def add(self,z):
        print(self.a+self.b+z)
obj = hello()
obj.add(50)
print(hello.a+hello.b)
hello.add(obj,100)
