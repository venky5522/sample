class Encapsulation:
    a = "hello"
    _a = "python"
    __a = "welcome"
    def hello(self):
        print("in hello method")
    def welcome(self):
        print("in welcome method")
    def __abc(self):
        print("in private method")
obj = Encapsulation()
#print(dir(obj))
print(obj.a)
print(obj._a)
#print(obj.__a)
obj.hello()
obj.welcome()
print(obj._Encapsulation__a)
obj._Encapsulation__abc()