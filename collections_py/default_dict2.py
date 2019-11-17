'''l = [1,2,3,4,5,4,3,2,4,5,3,2]
a = {}
for i in l:
    if i not in a:
        a[i] = l.count(i)
print(a)'''
from collections import defaultdict
l = [1,2,3,4,5,4,3,2,4,5,3,2]
d = defaultdict(int)
for i in l:
    d[i[0]]+=1
print(d)



