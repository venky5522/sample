def outer(a):
    print("i am outer function")
    def inner():
        print(a)
        print("i am inner function")
    return inner
obj = outer(1000)
obj()

