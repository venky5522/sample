import os
Get_path = r"C:\Users\pravallika p\PycharmProjects\classprograms\file_handling"
os.chdir(Get_path)
a = os.listdir()
for i in a:
    file_name,file_ext = os.path.splitext(i)
    #print(file_name)
    print(file_ext)



