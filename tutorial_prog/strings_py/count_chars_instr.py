a = "google.com"
d = {}
for i in a:
    key = d.keys()
    if i in key:
        d[i]+=1
    else:
        d[i] = 1
print(d)





