str = "the quick brown fox jumps over the lazy dog"
words = str.split()
print(words)
count = {}
for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(count)
