def extend_list(val,list=[]):
    list.append(val)
    return list
list1 = extend_list(10)
list2 = extend_list(123,[])
list3 = extend_list("a")
list4 = extend_list("b")
print(list1,list2,list3,list4)


