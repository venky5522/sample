Get_path = r"C:\Users\pravallika p\PycharmProjects\Class Programs\python.py"
try:
    with open(Get_path,"w") as my_file:
        text = my_file.write("hello venkatesh\nhello python")
        print("file write successfully")
except IOError:
    print("file not existed!!!!")
else:
    print("else block get executed!!!!")
finally:
    print("finally block get executed!!!!")
    my_file.close()
    print("file closed successfully!!!!")
