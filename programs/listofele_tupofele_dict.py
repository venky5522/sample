l = [10,20,30,40,50]
t = (1,2,3,4,5)
d = {}
'''for i in enumerate(t):
    d[i[1]] = l[i[0]]
print(d)'''
for i in range(len(l)):
    d[t[i]] = l[i]
print(d)
