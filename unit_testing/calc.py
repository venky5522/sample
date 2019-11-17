def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def division(a,b):
    if b==0:
        raise ValueError('b value must be greater than 0')
    return a/b
