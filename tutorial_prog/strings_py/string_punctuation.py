from string import punctuation
string = "hello there... iam learning python !"
new_string = " "
for i in string:
    if i not in punctuation:
        new_string = new_string+i
print(new_string)



