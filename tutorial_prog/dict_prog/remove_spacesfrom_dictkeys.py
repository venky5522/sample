student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
print("Original dictionary: ",student_list)
d = {}
for key,value in student_list.items():
    key = key.split()
    d["".join(key)] = value
print("new dictionary is: ",d)


