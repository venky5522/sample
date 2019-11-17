a = "hello"
b = 100
try:
    c =a+b
    print(c)
    print("try block get executed!!!!")
except:
    d = a+str(b)
    print(d)
    print("except block get executed!!!!")
else:
    print("else block get executed!!!!")
finally:
    print("finally block get executed!!!!")