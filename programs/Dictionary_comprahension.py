'''a = [1,2,3,4,5,6,7,8,9]
b = {i:i**2 for i in a}
print(b)'''
'''d = {'a':10, 'b': 34,'z':35,'B':10, 'A': 7, 'Z':3}
out = {k.lower(): d.get(k.lower(), 0) + d.get(k.upper(), 0) for k in d}
print(out)'''
my_dict = {'a':1,'b':2,'c':3}
a = {value:key for key, value in my_dict.items()}
print(a)




