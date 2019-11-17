l = [23,4,45,66,5,4,33,7,8,2,3]
l1 = []
def second_smallest(l):
    for i in l:
        if i not in l1:
            l1.append(i)
            l1.sort()
    if len(l1) >1:
        print(l1[1])
    else:
        pass
print(second_smallest(l))









