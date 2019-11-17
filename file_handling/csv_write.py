import csv
Get_path=r"C:\Users\pravallika p\Desktop\CSVsamle.csv"
with open(Get_path,'w',newline="") as csvfile:
    csv_writer=csv.writer(csvfile)
    csv_writer.writerow(["empid","ename","eage","esal"])
    for i in range(1):
        csv_writer.writerow([10,"venky",23,10000])
        csv_writer.writerow([20,"lokesh",24,20000])
        csv_writer.writerow([30,"anvesh",25,30000])
        csv_writer.writerow([40,"chaitu",26,40000])
        csv_writer.writerow([50,"babu",27,50000])




