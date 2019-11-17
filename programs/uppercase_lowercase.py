string = "The Quick Brown Fox Jumps Over The Lazy Dog"
count1= 0
count2 = 0
for i in string:
    if(i.isupper()):
        count1 = count1+1
    elif(i.islower()):
        count2 = count2+1
print("total upper case letters are: ",count1)
print("total lower case letters are: ",count2)



