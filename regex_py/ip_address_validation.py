n = input("enter the ip address: ")
list1 = n.split('.')
count = 0
if len(list1) == 4:
    for i in list1:
        if int(i)>=0 and int(i)<=255:
            count = count+1
if count == 4:
    print(n,"is a valid ip")
else:
    print(n,"is not a valid ip")







