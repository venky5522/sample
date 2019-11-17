def hello(fn):
    def welcome(x,y):
        if x>0 and y>0:
            z = fn(x,y)
            return z
        else:
            print("numbers is greater than zero!!!!")
    return welcome

def addition(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

val = hello(addition)
p = val(10,20)
print(p)