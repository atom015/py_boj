n,p,q = map(int,input().split())
a = [0 for i in range(100000+1)]
a[0] = 1
def dp(n):
    if n < 100000 and a[n] > 0:return a[n]
    if n < 100000:
        a[n] = dp(n//p)+dp(n//q)
        return a[n]
    return dp(n//p)+dp(n//q)
print(dp(n))
