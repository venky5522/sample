str1 = "Hello there! Whats up"
str2 = "Hello there! How are you"
count = {}
for word in str1.split():
    count[word] = count.get(word,0)+1
print(count)
for word in str2.split():
    count[word] = count.get(word,0)+1
print(count)
print([word for word in count if count[word] == 1])
