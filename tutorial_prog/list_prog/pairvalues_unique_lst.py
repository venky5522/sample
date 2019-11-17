lst = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),(7, 8), (9, 10)]
ls = []
for x in lst:
    for y in x:
        if y not in ls:
            ls.append(y)
print(ls)

