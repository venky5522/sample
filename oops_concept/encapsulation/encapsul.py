class Encapsulation:
    a = "hello"
    _a = "python"
    __a = "welcome"
print(Encapsulation.a)#hello
print(Encapsulation._a)#python
#print(Encapsulation.__a) we cant print private variable out side of a class