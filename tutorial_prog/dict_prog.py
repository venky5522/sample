Get_path = r"C:\Users\pravallika p\Desktop\SampleCSVFile_2kb.csv"
import csv
valid_data = open('valid.txt','w')
invalid_data = open('invalid.txt','w')
duplicate_data = open('duplicate.txt','w')
special_chars = "!@#$%^&*"
l = []

with open(Get_path) as my_file:
    read_data = csv.reader(my_file)
    for i in read_data:
        if i is special_chars:
            invalid_data.write(i)
        else:
            valid_data.write(str(i))


