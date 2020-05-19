from sys import *
ip = stdin.readline

n = 2000000
a = [0, 0] + [1] * (n - 1)
primes = []
for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(i, n + 1, i):
            a[j] = 0

def isPrime(n):
    for i in primes:
        if i >= n:break
        elif not n % i:
            return 0
    return 1

for i in range(int(ip())):
    a,b = map(int,ip().split())
    s = a+b
    if s < 4:
        print("NO")
    elif s % 2 == 0:
        print("YES")
    else:
        if isPrime(s-2):
            print("YES")
        else:
            print("NO")
