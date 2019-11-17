import csv
Get_path=r"C:\Users\pravallika p\Desktop\CSVsamle.csv"
with open(Get_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
csv_file.close()




