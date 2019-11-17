Get_path = r"C:\Users\pravallika p\PycharmProjects\classprograms\trail.py"
with open(Get_path) as my_file:
    empty_dict = {}
    for i in my_file:
        a = i.strip().split()
        for j in a:
            if j not in empty_dict.keys():
                empty_dict[j] = 1
            else:
                empty_dict[j]+=1
count,word = 0,0
for key in empty_dict.keys():
    if empty_dict[key]>count:
        count = empty_dict[key]
        word = key
print(word,':',count)