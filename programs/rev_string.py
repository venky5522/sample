# my_str = "welcome to python"
# my_split = my_str.split(' ')
# my_split.reverse()
# my_join = ' '.join(my_split)
# print(my_join)

my_str = "welcome to python"
a = my_str.split()
i = len(a)-1
str = " "
while i>=0:
    str = str+" "+a[i]
    i = i-1
print(str)
