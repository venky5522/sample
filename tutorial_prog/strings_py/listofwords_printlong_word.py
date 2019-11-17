'''a = ["apple","orange","mango","bananaa"]
b = ""
for i in a:
    if len(i)>len(b):
        b = i
print("longest word is: ",b)'''

a = ["apple","orange","mango","bananaa"]
b = []
for i in a:
    b.append((len(i),i))

print(b)
b.sort(reverse=True)
print("longest word is: ",b[0][1])
