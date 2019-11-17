def hello(fn):
    def welcome(x,y):
        if x>0 and y>0:
            z = fn(x,y)
            return z
        else:
            print("numbers must be greater than zero")
    return welcome
@hello
def addition(a,b):
    return a+b
@hello
def substraction(a,b):
    return a-b
@hello
def multilication(a,b):
    return a*b
@hello
def division(a,b):
    return a/b

val = addition(10,20)
print(val)
val = substraction(10,20)
print(val)
val = multilication(10,20)
print(val)
val = division(10,2)
print(val)