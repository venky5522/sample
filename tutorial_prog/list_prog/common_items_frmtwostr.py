color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
a = []
for i in color1:
    for j in color2:
        if i == j:
            a.append(i)
print(a)
