Get_path = r"C:\Users\pravallika p\PycharmProjects\Class Programs\python.py"
try:
    my_file = open(Get_path,"r")
    text = my_file.readlines()
    #text = my_file.readlines(1)
    print(text)
    print("file read successfully")
except IOError:
    print("file not existed!!!!")
else:
    print("else block get executed!!!!")
finally:
    print("finally block get executed!!!!")
    my_file.close()
    print("file closed successfully!!!!")
