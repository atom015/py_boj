n,k = map(int,input().split())
def fa(n):
    tmp = 1
    for i in range(1,n+1):
        tmp *= i
    return tmp
ans = fa(n) // (fa(k)*fa(n-k))
print(ans%10007)
