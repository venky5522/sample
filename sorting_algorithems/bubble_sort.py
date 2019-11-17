nlist = [14,46,43,27,57,41,45,21,70]

def bubble_sort(nlist):
    for val in range(len(nlist)-1,0,-1):
        for i in range(val):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
bubble_sort(nlist)
print(nlist)

