# n = int(input("enter your number: "))
# a=1
# for i in range(1,n+1):
#     a=a*i
# print(a)

#factorial of a number upto n.
n=int(input("enter your number: "))
for i in range(n+1):
    a=1
    for j in range(1,i+1):
        a=a*j
    print("the factorial of",i,"is",a)



