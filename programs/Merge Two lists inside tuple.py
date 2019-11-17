# a=[1,2,3,4]
# b=[5,6,7,8]
# c=[]
# for i in range(max(len(a),len(b))):
#     venky = (a[i],b[i])
#     c.append(venky)
# print(c)

def merge(a,b):
    my_list = list(zip(a,b))
    return my_list
a=[1,2,3,4]
b=[5,6,7,8]
print(merge(a,b))