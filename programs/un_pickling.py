import pickle
with open('pickl.py','rb') as x:
    my_file = pickle.load(x)
    for i in my_file:
        print(i)
