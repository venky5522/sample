test_list1 = [1, 5, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]

my_len1 = len(test_list1)
my_len2 = len(test_list2)

res = []
i,j = 0,0

while i<my_len1 and j<my_len2:
    if test_list1[i] < test_list2[j]:
        res.append(test_list1[i])
        i +=1
    else:
        res.append(test_list2[j])
        j +=1
res = res + test_list1[i:] + test_list2[j:]
print("merge and sort list is: "+str(res))
