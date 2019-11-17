lcount = int(input("enter the lcount: "))
ucount = int(input("enter the ucount: "))
for num in range(lcount,ucount+1):
    rev = int(str(num)[::-1])
    if num == rev:
        if num>1:
            for i in range(2,num):
                if(num % 2 ==0):
                    break
            else:
                print(num)

