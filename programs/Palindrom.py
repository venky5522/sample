n = input("enter the string: ")
a=list(n)
b=list(reversed(a))
if(a==b):
    print(n,"is a palindrom")
else:
    print(n,"is not a palindrom")