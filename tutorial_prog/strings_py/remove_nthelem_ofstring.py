'''a = input("enter any string: ")
b=list(a)
c= int(input("enter the nth index: "))
b.pop(c)
z = "".join(b)
print(z)'''

string = "venkatesh"
n = int(input("enter index: "))
empty_string = " "
for i in range(len(string)):
    if i !=n:
        empty_string = empty_string + string[i]
print(empty_string)


