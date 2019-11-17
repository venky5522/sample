class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
class B(A):
    def __init__(self,n,m):
        self.name = n
    def get_age(self):
        return self.age
class C(B):
    def get_age(self):
        return "abcd"
obj = C("venky","babu")
print(obj.get_name())
print(obj.get_age())
