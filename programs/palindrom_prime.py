'''num = int(input("enter the number: "))
rev = int(str(num)[::-1])
print("the reversed number is: ",rev)
if num == rev:
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                print(num,"it is not a prime number and it is palindrom")
                break
        else:
            print(num,"it is a palindromic prime number")
else:
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                print(num,"it is not a prime number as well as it is not a palindrom")
                break
        else:
            print(num,"it is a prime number and it is not a palindrom")'''
#palindrom prime numbers upto some range.

lower = int(input("enter lower number: "))
upper = int(input("enter upper number: "))
for num in range(lower, upper+1):
    rev = int(str(num)[::-1])
    if num == rev:
        if num>1:
            for i in range(2,num):
                if(num%i==0):
                    break
            else:
                print(num)
