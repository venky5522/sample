class A:
    def __init__(self):
        print("in INIT method")
    def hello(self):
        print("in hello method")
class B(A):
    def welcome(self):
        print("in welcome method")
obj = B()
obj.welcome()
obj.hello()