cnt = 1
while 1:
    l,p,v = map(int,input().split())
    if l == p == v == 0:break
    if l >= v%p:
        ans = (v//p)*l+v%p
    else:
        ans = (v//p)*l+l
    print("Case {}: {}".format(cnt,ans))
    cnt += 1
