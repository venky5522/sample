Get_path = r'C:\Users\pravallika p\PycharmProjects\classprograms\trail.py'
n = int(input("enter: "))
with open(Get_path,'r') as my_file:
    count = 0
    for i in my_file:
        count+=1
        if count == n+1:
            break
        print(i)

