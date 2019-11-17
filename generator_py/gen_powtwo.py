def my_gen(max = 0):
    n = 0
    while n<max:
        yield 2**n
        n+=1
p = my_gen(10)
print(p)
it = iter(p)
for n in it:
    print(n)




