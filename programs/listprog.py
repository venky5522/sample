a = [1, 2, 3]
b = [4, 5, 6]
#o/p: [(1, 16), (2, 25), (3, 36)]

c = []
if len(a) == len(b):
    for i in range(len(a)):
        c.append((a[i], b[i] ** 2))
    print(c)
else:
    print("Both the lists should be of same length")

