n,m = map(int,input().split())
n1,m2 = n,m
while 1:
    if m != 0:
        r = n%m
        n = m
        m = r
    else:
        print(n)
        print(int(n1*m2/n))
        break
