import csv
Get_path=r"C:\Users\pravallika p\Desktop\CSVsamle.csv"
with open(Get_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    empty_dict = {}
    for row in csv_reader:
        empty_dict[row[0]] = row[1],row[2],row[3]
user_resp = input("enter the empid: ")
if user_resp in empty_dict:
    print(empty_dict[user_resp])
else:
    print("please enter the correct empid")
    print("please try again")



