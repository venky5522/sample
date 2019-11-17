string = "venkateshbabuprattipati"
d = {}
for i in string:
    key = d.keys()
    if i in key:
        d[i]+=1
    else:
        d[i] = 1
print(d)

