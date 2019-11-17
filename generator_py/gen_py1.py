def my_gen():
    yield "hello"
    yield "python"
    yield "welcome"
    yield 10
a = my_gen()
#print(a)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

