def make_prety(func):
    def inner():
        print("i am inner function!!!!")
        func()
    return inner
@make_prety
def ordinary():
    print("i am ordinary function!!!!")
ordinary()



