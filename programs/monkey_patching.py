import monk
def monkey_f(self):
    print("This is monkey patching")
monk.A.func = monkey_f
obj = monk.A()
obj.func()
