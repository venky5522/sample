'''n = int(input("enter your number: "))
tag = 0
for i in range(1,n+1):
    if(n%i==0):
        tag = tag+1
if(tag==2):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")'''

#print prime numbers upto n.

# n = int(input("Enter Your Number: "))
# tag = 0
# for i in range(n+1):
#     a=0
#     for j in range(1,i+1):
#         if(i%j==0):
#             a=a+1
#     if(a==2):
#         tag = tag+1
#         print("Number",i,"is a prime number")
# print(tag,"prime numbers are existed")

# prime numbers range uto 100.
n = int(input("Enter your number: "))
for i in range(2,n+1):
    for j in range(2,i):
        if(i%j==0):
            print("{} is not a prime number".format(i))
            break
    else:
        print("{} is a prime number".format(i))
