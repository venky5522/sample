Get_path = r'C:\Users\pravallika p\PycharmProjects\classprograms\trail.py'
string = "venky"
with open(Get_path) as my_file:
    for num,line in enumerate(my_file,1):
        if string in line:
            print("string available in: ",num)




