d = {'hundred': 100, 'five': 5, 'ten': 10, "six": 6, "thirty": 30}
l = []
for k,v in d.items():
    l.append(v)
    l.sort(reverse=True)
print(l[0:3])

