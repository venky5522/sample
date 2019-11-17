def lcm(a,b):
    lcm.multiple = lcm.multiple+b
    if((lcm.multiple % a == 0) and (lcm.multiple % b == 0)):
        return lcm.multiple
    else:
        lcm(a,b)
        return lcm.multiple
lcm.multiple = 0
a=int(input("enter the number of a: "))
b=int(input("enter the number of b: "))
if(a>b):
    LCM=lcm(b,a)
else:
    LCM=lcm(a,b)
print(LCM)
