Get_path = r'C:\Users\pravallika p\PycharmProjects\classprograms\trail.py'
with open(Get_path,'r') as my_file:
    for i, line in enumerate(my_file):
        if i==6:
            #it will print 7th line
            break
print(line)