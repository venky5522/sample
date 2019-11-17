vowels = "aeiou"
my_str = "Hello you have Tried our Tutorial section yet!!!!"
my_str = my_str.casefold()
count = {}.fromkeys(vowels,0)
for char in my_str:
    if char in count:
        count[char]+=1
print(count)







