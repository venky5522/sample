list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
for i in list1:
    if i not in list2:
        print("missing values in list2 is : ",i)
for j in list2:
    if j not in list1:
        print("additional values in list2 is : ",j)

