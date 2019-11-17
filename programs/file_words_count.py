Get_path = r"C:\Users\pravallika p\PycharmProjects\classprograms\trail.py"
file = open(Get_path)
words = file.read()
words_count = {}
for word in words.split():
    if word not in words_count:
        words_count[word] = 1
    else:
        words_count[word]+=1
print(words_count)





