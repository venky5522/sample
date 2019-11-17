Get_path = r'C:\Users\pravallika p\PycharmProjects\classprograms\trail.py'
with open(Get_path,'r') as my_file:
    for i, line in enumerate(my_file,1):
        if i==6:
            break
print(line)


