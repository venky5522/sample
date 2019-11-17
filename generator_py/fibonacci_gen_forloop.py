def my_gen(n):
    a,b = 0,1
    for i in range(n+1):
        yield a
        a,b = b,a+b
c = my_gen(50)
print(c)
for j in c:
    print(j)
