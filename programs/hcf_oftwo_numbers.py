def hcf_two(x,y):
    while(y):
        x,y = y,x%y
    return x
HCF = hcf_two(400,24)
print("HCF is: ",HCF)