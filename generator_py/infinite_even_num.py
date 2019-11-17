def my_gen():
    n = 0
    while True:
        yield n
        n+=2
p = my_gen()
it = iter(p)
for i in it:
    print(i)