a = "python"
b = "selenium"
x=0
for i in a:
    print(i)
    if(x<len(b)):
        print(b[x])
        x+=1
while(x<len(b)):
    print(b[x])
    x+=1