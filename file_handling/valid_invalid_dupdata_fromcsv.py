import re
import csv
Get_path = r"C:\Users\pravallika p\Desktop\SampleCSVFile_2kb.csv"
l = []
d = {}
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
with open(Get_path) as my_file:
    valid = open('valid_data.txt','w')
    invalid = open('invalid_data.txt','w')
    duplicate = open('duplicate_data.txt','w')
    csv_reader = csv.reader(my_file)
    for i in csv_reader:
        for j in i:
            if (regex.search(j) == None):
                valid.write(" "+j)
            else:
                invalid.write(" "+j)
        for x in i:
            l.append(x)
for y in l:
    d[y] = l.count(y)
for k,v in d.items():
    if v>1:
        duplicate.write(" "+k)
print("!!!!!Successfully Task Completed!!!!!")
print("Thank You")












