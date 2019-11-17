def method_dec(method):
    def inner(city_instance):
        if city_instance.name == "SFO":
            print("it is cool place to live")
        else:
            print("it is not cool place to live")
    return inner
class city(object):
    def __init__(self,name):
        self.name = name
    @method_dec
    def print_dec(self):
        print(self.name)
obj = city("SFO")
obj.print_dec()