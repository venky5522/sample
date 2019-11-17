list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
empty_list = []
val = list(zip(list2,list1))
val.sort()
for i in val:
    empty_list.append(i[1])
print(empty_list)


