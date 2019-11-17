'''string = "the quick brown fox jumps over the lazy dog"
string=string.casefold()
string=set(string)
if(len(string) == 27 and " " in string):
    print("this is a pangram!!")
else:
    print("this is not a pangram")'''

my_string = "the quick brown fox jumps over the lazy dog"
def pangram(string):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    empty_str = " "
    for word in string:
        for letter in alphabets:
            empty_str+=word
    for word in alphabets:
        if word not in empty_str:
            return False
    else:
        return True
print(pangram(my_string))

'''my_string = "the quick brown fox jumps over the lazy dog"
def pangram(string):
    c=0
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    empty_string =" "
    for word in string:
        for letter in alphabets:
            if word == letter and word not in empty_string:
                empty_string+=word
    for word in empty_string:
        for letter in alphabets:
            if word == letter:
                c+=1
    if c==26:
        return True
    else:
        return False
print(pangram(my_string))'''