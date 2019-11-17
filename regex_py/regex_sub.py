import re
str1 = "raju@abc.com and babu@123.com and venky@gmail.com"
mat = re.sub(r"@\w+" ,"@gmail",str1)
print(mat)
