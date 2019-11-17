def smart_division(func):
    def inner(a,b):
        print("i am going to divide",a,"and",b)
        if b == 0:
            print("b canot be divided by zero")
            return
        return func(a,b)
    return inner
@smart_division
def division(a,b):
    return a/b
'''val = smart_division(division)
print(val)
babu = val(10,0)
print(babu)'''
val = division(10,20)
print(val)


