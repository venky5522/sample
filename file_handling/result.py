import math
import os
Get_path = r"C:\Users\pravallika p\PycharmProjects\classprograms\trail.py"
a = os.stat(Get_path)
b = a.st_size
def convert_size(b):
    if b==0:
        return "0B"
    size_names = ("B","KB","MB","GB","TB","PB","EB","ZB","YB")
    i = int(math.floor(math.log(b,1024)))
    p = math.pow(1024,i)
    s = round(b/p,2)
    return "%s %s" % (s,size_names[i])
print(convert_size(b))