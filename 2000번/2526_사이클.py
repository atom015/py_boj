n,p = map(int,input().split())
chk = []
ans = []
tmp,tmp2 = n,0
while 1:
    n = (n*tmp)%p
    if n in chk:
        tmp2 = n
        break
    chk.append(n)
print(len(chk[chk.index(tmp2):]))
