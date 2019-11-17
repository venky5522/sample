a = ['ashok', 'hari', 'bhanu', 'anil', 'bharath', 'anvesh', 'uday', 'raja']
d = {}
for i in a:
    s = i.split()
    if i[0] not in d:
        d[i[0]] = []
    d[i[0]].append(i)
print(d)
