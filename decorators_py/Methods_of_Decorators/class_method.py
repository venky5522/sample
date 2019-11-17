class Decorator:
    def __init__(self):
        print("INIT based function")
    @classmethod
    def class_based_decorator(cls):
        print("This is class based function")
        cls.static_based_decorator()
    @staticmethod
    def static_based_decorator():
        print("This is static based function")
de = Decorator()
de.class_based_decorator()
