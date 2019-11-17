d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'c': 200, 'b':400}
c = {}
for i in d1.keys():
    for j in d2.keys():
        if i==j:
            c.update({i:d1[i]+d2[i]})
        else:
            c.update({j:d1[j]+d2[j]})
print(c)







