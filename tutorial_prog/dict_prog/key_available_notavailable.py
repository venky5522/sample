d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key_check(x):
    if x in d:
        print("key is available in dict")
    else:
        print("key is not available in dict")
key_check(4)
key_check(5)
key_check(7)
