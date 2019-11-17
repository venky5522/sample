def largest_num(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
print(largest_num([1,2,4,6,5,33,54,6,9]))






