color = ['Red', 'Green', 'Black']
ls = []
for x in color:
    for y in ('c',x):
        ls.append(y)
print(ls)

lst = [1,2,3,4,5,6,7,8,9]
l = []
p = len(lst)
n = 5
for i in range(p):
    l.append(n)
    l.append(lst[i])
print(l)



