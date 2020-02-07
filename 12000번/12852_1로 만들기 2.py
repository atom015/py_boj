n = int(input())
v = [False for i in range((10**6)+1)]
q = [[n,[n],0]]
while q:
    now,load,cnt = q.pop(0)
    if now == 1:
        print(cnt)
        print(*load)
        break
    if 0 <= now-1 < 10**6 and v[now-1] == False:
        q.append([now-1,load+[now-1],cnt+1])
        v[now-1] = True
    if now % 3 == 0 and v[now//3] == False:
        q.append([now//3,load+[now//3],cnt+1])
        v[now//3] = True
    if now % 2 == 0 and v[now//2] == False:
        q.append([now//2,load+[now//2],cnt+1])
        v[now//2] = True
