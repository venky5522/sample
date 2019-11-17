l = [3,22,33,4,6,8,3,44,5,77]
def selection_sort(l):
    for i in range(len(l)):
        min = i
        for j in range(i+1,len(l)):
            if l[min]>l[j]:
                min = j
        l[i],l[min] = l[min],l[i]
    return l
print(selection_sort(l))



