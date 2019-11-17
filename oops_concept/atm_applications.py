print("Welcome To HDFC Bank ATM!!!!")
pin = int(input("Enter your pin: "))
while True:
    if pin == 5522:
        print("Access Granted!!!!")
        print("1.Balance\n"
              "2.Withdraw\n"
              "3.Deposit\n"
              "4.Quit")
        break
    else:
        print("Try Again!!!!")
        break
balance = 10000
option = int(input("enter your option"))
if option == 1:
    print("your account balance is: ",balance)
if option == 2:
    print("your account balance is: ",balance)
    withdraw = int(input("enter the withdraw balance: "))
    if withdraw>0:
        result = balance-withdraw
        print("your account balance is: ", result)
    elif withdraw>balance:
        print("Insufficients funds in your account")
if option == 3:
    print("your account balance is: ",balance)
    deposit = int(input("enter the deposit amount: "))
    result1 = balance+deposit
    print("your account balance is: ",result1)
if option == 4:
    exit()









