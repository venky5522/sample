import re
n = "hello venky_p@gmail.com"
mat = re.search('([\w.-]+)@([\w.-]+)',n)
if mat:
    print(mat.group())
    print(mat.groups())


