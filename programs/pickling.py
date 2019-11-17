import pickle
data = [['scott',7788,5666,3455],
        ['venky',3344,2233,5544],
        ['loki',8877,5544,2211]]
x = None
try:
    my_file = open('pickl.py','wb')
    print("file opened successfully")
    pickle.dump(data,my_file)
except:
    print("error occured")
finally:
    if x!=None:
        x.close()

