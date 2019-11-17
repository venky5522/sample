a = ["sachin cricket", "Federer tennis", "Nadal tennis", "virat cricket", "Messi football"]
d = {}
for i in a:
    s = i.split()
    if s[1] not in d:
        d[s[1]] = []
    d[s[1]].append(s[0])
print(d)