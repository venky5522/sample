def inner(m):
    def outer(n):
        z = m*n
        return z
    return outer
'''val = inner(10)
babu = val(20)
print(babu)'''
val = inner(10)(20)
print(val)

