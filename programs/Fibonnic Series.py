# n=int(input("enter your number: "))
# a=0
# b=1
# i=0
# if n<=0:
#     print("enter positive number!!")
# elif n==1:
#     print("the fibonnic series are",n)
#     print(a)
# else:
#     print("the fibonnic series upto",n)
#     while i<=n:
#         print(a,end=" ")
#         nth = a + b
#         a=b
#         b=nth
#         i = i+1

#Fibonicc Series.
n = int(input("enter your number: "))
a=0
b=1
print(a)
print(b)
i=0
while True:
    i = i+1
    if (i<=n):
        c=a+b
        if c == 55:
            break
        print(c)
        a=b
        b=c
    else:
        print("Successfully executed")
        break