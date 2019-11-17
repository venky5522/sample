'''my_dict = {'x':1,'y':2,'z':3}
d= {}
for i,j in my_dict.items():
    d[j] = i
print(d)'''
my_dict = {'x':1,'y':2,'z':3}
for i in my_dict.keys():
    my_dict[my_dict.pop(i)] = i
print(my_dict)

