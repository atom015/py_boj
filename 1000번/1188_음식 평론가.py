def uclid(n,m):
    if n < m:
        n,m = m,n
    if n%m == 0:
        return m
    return uclid(m,n%m)
n,m = map(int,input().split())
print(m-uclid(n,m))
