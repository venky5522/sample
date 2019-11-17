words = ["act", "tea", "node", "ate", "cat", "done", "tab", "eat", "xyz", "bat"]
sorted_word = {}
for word in words:
    sorted_word[word] = ''.join(sorted(word))
print(sorted_word)
anagrams = []
for i in range(len(words)):
    ana = [words[i]]
    for j in range(i+1,len(words)):
        if sorted_word[words[i]] == sorted_word[words[j]]:
            ana.append(words[j])
    if len(ana) !=1:
        anagrams.append(ana)
print(anagrams)
