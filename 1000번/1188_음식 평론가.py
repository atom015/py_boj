def uclid(n,m):
    if n < m:
        n,m = m,n
    while 1:
        if m == 0:
            return n
        tmp = n
        n = m
        m = tmp%m
n,m = map(int,input().split())
print(m-uclid(n,m))
