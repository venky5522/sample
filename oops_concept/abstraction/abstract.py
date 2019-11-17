from abc import abstractmethod, ABCMeta
class Abstract(metaclass=ABCMeta):
    def abc(self):
        print("in abc method")
    @abstractmethod
    def hello(self):
        pass
    @abstractmethod
    def welcome(self):
        pass
class Derived(Abstract):
    def hell(self):
        print("in hell method")
    def hello(self):
        print("in hello method")
    def welcome(self):
        print("in welcome method")
obj = Derived()
print(obj)
obj.hell()
obj.hello()
obj.welcome()


