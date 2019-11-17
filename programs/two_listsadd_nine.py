a=[1, 2, 4, 5, 7]
b=[5, 6, 3, 4, 8]
c=[]
for i in a:
    for j in b:
        if i+j == 9:
            c.append((i,j))
print(c)


