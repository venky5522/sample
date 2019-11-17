import queue

L = queue.Queue(maxsize=20)

L.put(9)
L.put(4)
L.put(7)
L.put(6)
L.put(2)

print(L.get())
print(L.get())
print(L.get())
print(L.get())
print(L.get())