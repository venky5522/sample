class Decorator:
    def __init__(self):
        print("INIT based method")
    @staticmethod
    def Example_method():
        print("This is static method")
        print("End the static method")
de = Decorator()
de.Example_method()



