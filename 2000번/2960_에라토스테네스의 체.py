n,m = map(int,input().split())
a = [False,False] + [True]*(n-1)
primes=[]
result = []

for i in range(2,n+1):
    if a[i]:
        primes.append(i)
    for j in range(i, n+1, i):
        if a[j] == True:
            result.append(j)
        a[j] = False
print(result[m-1])
