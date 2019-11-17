from collections import defaultdict
a = "mississippi"
d = defaultdict(int)
for i in a:
    d[i]+=1
print(d)



