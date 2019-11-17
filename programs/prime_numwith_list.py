l = [1,2,3,4,5,6,7,8,9]
l1 = []
for i in l:
    if i>=2:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            l1.append(i)
print(l1)
