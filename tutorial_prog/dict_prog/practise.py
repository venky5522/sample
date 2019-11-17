a = "google.com"
d = {}
for i in a:
    b = d.keys()
    if i in b:
        d[i]+=1
    else:
        d[i] = 1
print(d)