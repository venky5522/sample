l = [1,2,3,3,3,3,4,5]
a= []
for i in l:
    if i not in a:
        a.append(i)
print(a)