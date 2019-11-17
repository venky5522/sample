def mak_multifier(m):
    def welcome(n):
        return m*n
    return welcome
times1 = mak_multifier(9)
times2 = mak_multifier(5)
times3 = mak_multifier(7)
print(times1(3))
print(times2(4))
print(times3(5))


