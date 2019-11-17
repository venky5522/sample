def common_items(l1,l2):
    result = False
    for i in l1:
        for j in l2:
            if i == j:
                result = True
    return result
print(common_items([1,2,3,4],[1,2,3]))




