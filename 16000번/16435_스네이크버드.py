n,h = map(int,input().split())
fu = list(map(int,input().split()))
chk = [False for i in range(n)]
for i in range(n):
    for j in range(n):
        if fu[j] <= h and chk[j] is False:
            chk[j] = True
            h += 1
print(h)
