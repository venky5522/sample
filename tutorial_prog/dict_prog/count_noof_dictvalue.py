d =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
'''l = []
for i in d.values():
    l.append(i)
a = len(l[0]+l[1])
print("count of the dictionary values are: ",a)'''
count = 0
for i in d:
    for x in d[i]:
        count+=1
print(count)

