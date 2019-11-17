my_str = ["babu",1,2,3,"venky","hi",5]
a=[]
b=[]
for i in my_str:
    if type(i) == int:
        a.append(i)
    if type(i) == str:
        b.append(i)
print(a)
print(b)