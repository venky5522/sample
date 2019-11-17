words = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
empty_list = []
for i in words:
    if words.index(i) not in (0,2,5):
        empty_list.append(i)
print(empty_list)





