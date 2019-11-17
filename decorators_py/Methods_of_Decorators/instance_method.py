class Decorator:
    def __init__(self):
        print("INIT based function")
        self.name = "This is instance method"
    def Example_Decorator(self):
        print("This is instance Method")
        print("Name is "+self.name)
de = Decorator()
de.Example_Decorator()
