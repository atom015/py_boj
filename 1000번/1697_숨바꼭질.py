n,k = map(int,input().split())
q = [[n,0]]
v = [False for i in range(100001)]
v[n] = True
while q:
    p,cnt = q.pop(0)
    if p == k:
        print(cnt)
        break
    if 0 <= p-1 and v[p-1] == False:
        q.append([p-1,cnt+1])
        v[p-1] = True
    if  p+1 <= 100000 and v[p+1] == False:
        q.append([p+1,cnt+1])
        v[p+1] = True
    if  p*2 <= 100000 and v[p*2] == False:
        q.append([p*2,cnt+1])
        v[p*2] = True
