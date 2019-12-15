a,b = map(int,input().split())
def sosu(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
      if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
    if n in primes:
        return True
def under_prime(n):
    cnt = 0
    i = 2
    while i*i <= n:
        while n % i == 0:
            cnt += 1
            n //=i
        i += 1
    if n > 1:
        cnt += 1
    if sosu(cnt):
        return True

cnt = 0
for i in range(a,b+1):
    if under_prime(i):
        cnt += 1
print(cnt)
