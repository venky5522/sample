l = [3,6,78,90,23,45]
x = 23
def linear_search(l,x):
    n = len(l)
    for i in range(0,n):
        if(l[i] == x):
            return i
    return -1
result = linear_search(l,x)
if result == -1:
    print(x,"Does not exit: ")
else:
    print(x,"position is: ",result)