class a:
    def hello(self,*args):
        print("hello")
obj = a()
obj.hello()
obj.hello(10)
obj.hello(10,20,30)
obj.hello(10,20,30,40)
