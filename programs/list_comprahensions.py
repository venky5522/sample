'''my_string = "welcome to python world"
my_cond = [len(i) for i in my_string.split(" ")]
print(my_cond)'''
'''num = [x **2 for x in range(10) if x%2==0]
print(num)'''
'''d = ["hello","welcome","to","python","world"]
a = [(i,len(i)) for i in d if len(i)>=4]
print(a)'''
'''a = [x for x in range(100) if x%3==0 if x%5==0]
print(a)'''
'''a = [10,3,4,5,20,30,40,25,14,24,16,17,18]
b = [x for x in a if x>10 if x<20]
print(b)'''
'''a = [1,2,3,4]
b = ["A","B","C","D"]
c = [str(i)+j for i in a for j in b]
print(c)'''
'''a = [1,2,3,4,5,6]
b = [4,5,6,7,8,9]
c = [i for i in a for j in b if i==j]
print(c)'''
'''matrix = [[1,2],[3,4],[5,6]]
a=[]
for i in range(2):
    b = []
    for row in matrix:
        b.append(row[i])
    a.append(b)
print(a)'''
'''matrix = [[1,2],[3,4],[5,6]]
a = [[row[i] for row in matrix]for i in range(2)]
print(a)'''
