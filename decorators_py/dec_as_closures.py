def hello(wrapped):
    def inner():
        print("i am inner function!!!!")
        wrapped()
    return inner
def ordinary():
    print("i am ordinary function!!!!")
#ordinary()
preety = hello(ordinary)
preety()




