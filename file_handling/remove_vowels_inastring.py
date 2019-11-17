string = input("enter the string: ")
vowels = ('a','e','i','o','u')
my_string = string
for i in string.lower():
    if i in vowels:
        my_string = my_string.replace(i,'')
print(my_string)
