l = [3, 5, 7, [9, 6, 2, [8, 1], 10], 4, 7]
a = []
def flatten_list(l):
    for i in l:
        if type(i) == list:
            flatten_list(i)
        else:
            a.append(i)
print("original list is: ",l)
flatten_list(l)
print("flatten list is: ",a)





