'''def get_prime(x):
    primes = []
    for a in range(1,10000):
        for b in range(2,a):
            if(a%b==0):
                break
        else:
            primes.append(a)
        if len(primes) == x:
            return primes
print(get_prime(10))'''
n = int(input("enter the number: "))
l = []
for a in range(1,10000):
    for b in range(2,a):
        if(a%b==0):
            break
    else:
        l.append(a)
    if len(l) == n:
        break
print(l)
