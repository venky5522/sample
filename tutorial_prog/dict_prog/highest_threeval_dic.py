d = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
l = []
for k,v in d.items():
    l.append((v,k))
l.sort(reverse=True)
a = []
for i in l:
    a.append(i[1])
print(a[:3])



