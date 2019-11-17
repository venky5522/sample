class ClassBasedDecoratorWithParms:
    def __init__(self,arg1,arg2):
        print("INIT function decorator with parms")
        print(arg1)
        print(arg2)
    def __call__(self,fn, *args, **kwargs):
        print("CALL based decorator with parms")
        def new_func(*args,**kwargs):
            print("function has been decorated, congratulations")
            return fn(*args, **kwargs)
        return new_func
@ClassBasedDecoratorWithParms("welcome","python")
def print_args_again(*args):
    for arg in args:
        print(arg)
print_args_again(1,2,3)
print_args_again(4,5,6)


