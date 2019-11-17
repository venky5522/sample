l = [24,5,6,74,5,7,8,3,2,44,78,9]
l1 = []
for i in l:
    for j in range(i):
        if i+j==11:
            l1.append((i,j))
print(l1)