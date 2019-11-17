a = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
b = [1, 2, 2, 3]
d = {}
for k,v in zip(a,b):
    d[k] = {v}
print(d)




