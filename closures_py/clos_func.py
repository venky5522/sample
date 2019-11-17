def hello():
    def welcome():
        return "welcome to python"
    return welcome
val = hello()
print(val())