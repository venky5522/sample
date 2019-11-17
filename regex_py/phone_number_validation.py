import re
n = input("enter your phone number: ")
pattern=r'^[6-9]\d{9}$'
mat = re.match(pattern,n)
if mat:
    print(n,": is a valid phone number")
else:
    print(n,": is not a valid phone number")
