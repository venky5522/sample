def outer():
    print("i am outer function")
    def inner():
        print("i am inner function")
    inner()
outer()