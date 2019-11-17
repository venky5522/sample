class hello:
    a = 10
    b = 20
    def instance_method(self,c):
        print(self.a+self.b+c)
    @instance_method
    def class_method(cls,c):
        print(cls.a+cls.b+c)
    @class_method
    def static_method(c):
        print(a+b+c)
obj = hello()
print(obj)