def recursion(l):
    sum = 0
    for i in l:
        if type(i) == list:
            sum = sum + recursion(i)
        else:
            sum = sum + i
    return sum
l = [1, 2, [3,4], [5,6]]
print("recursion of sum is: ",recursion(l))

