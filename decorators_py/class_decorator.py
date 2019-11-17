class ClassBasedDecorator:
    def __init__(self,function_to_decorate):
        print("INIT class based decorator")
        self.function_to_decorate = function_to_decorate
    def __call__(self, *args, **kwargs):
        print("CALL class based decorator")
        return self.function_to_decorate(*args,**kwargs)
@ClassBasedDecorator
def print_more_args(*args):
    for arg in args:
        print(arg)
print_more_args(1,2,3)
print_more_args(1,2,3)








