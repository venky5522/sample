n = int(input("enter the year: "))
if(n%4==0):
    if(n%100==0):
        if(n%400==0):
            print("{} it is a leap year".format(n))
        else:
            print("{} it is not a leap year".format(n))
    else:
        print("{} it is a leap year".format(n))
else:
    print("{} it is not a leap year".format(n))