a = [0,1,2,3,4,5,6,7,8,9]
for i in range(len(a)):
    if i%2 == 0:
        a[i],a[i+1] = a[i+1],a[i]

print(a)




