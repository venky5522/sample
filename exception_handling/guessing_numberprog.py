class ValueTooSmallError:
    pass
class ValueTooLargeError:
    pass
number = 10
while True:
    try:
        n = int(input("enter a number: "))
        if n<number:
            print("ValueTooSmallError")
        elif n>number:
            print("ValueTooLargeError")
        break
    except(ValueTooSmallError):
        print("value too small error")
    except(ValueTooLargeError):
        print("value too large error")
if n == number:
    print("congratulations you guessed it")
else:
    pass


