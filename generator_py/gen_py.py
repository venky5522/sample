def my_gen():
    n=1
    print("this is first printed")
    yield n
    n+=1
    print("this is printed second")
    yield n
    n+=1
    print("this is printed last")
    yield n
p = my_gen()
it = iter(p)
print(next(it))
print(next(it))
print(next(it))

