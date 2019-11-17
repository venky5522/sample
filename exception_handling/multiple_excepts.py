a=int(input("enter the number of a: "))
b=int(input("enter the number of b: "))
try:
    c = a/b
    print(c)
except ZeroDivisionError:
    print("b cant be zero!!!!")
except ValueError:
    #print(err.__class__.__name__,str(err))
    print("enter numerical numbers only!!!!")
except:
    print("error occured!!!!")