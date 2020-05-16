N = int(input())
a = [False,False]+[True]*(N+1)
primes,e,Sum,ans = [],0,0,0
# prime_number
for i in range(2,N+1):
    if a[i]:
        primes.append(i)
        for i in range(2*i,N+1,i):
            a[i] = False
# two pointer
for s in range(len(primes)):
    while e < len(primes) and Sum < N:
        Sum += primes[e]
        e += 1
    if Sum == N:
        ans += 1
    Sum -= primes[s]
print(ans)
