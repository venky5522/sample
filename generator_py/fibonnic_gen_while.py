def my_gen(limit):
    a,b = 0,1
    while a<limit:
        yield a
        a,b = b,a+b
c = my_gen(100)
print(c)
for j in c:
    print(j)