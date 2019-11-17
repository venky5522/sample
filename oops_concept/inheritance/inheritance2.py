class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
class B(A):
    def get_age(self):
        return self.age
obj = B("venky",24)
print(obj.get_name())
print(obj.get_age())
