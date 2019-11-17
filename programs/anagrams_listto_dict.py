words = ["car","me","rac","em","race","ecar"]
empty_dict = {}
for word in words:
    reversed_word = word[::-1]
    if reversed_word in words:
        empty_dict[word] = words.pop(words.index(reversed_word))
print(empty_dict)
