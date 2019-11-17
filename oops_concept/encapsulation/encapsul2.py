class person:
    def __init__(self):
        self.name = "venkatesh"
        self.__lname = "babu"
    def display(self):
        return self.name+' '+self.__lname
p = person()
print(p)
print(p.name)
print(p._person__lname)
print(p.display())
