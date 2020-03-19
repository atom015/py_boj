import sys
ip = sys.stdin.readline
n = int(ip())
m = int(ip())
arr = [[] for i in range(n+1)]
back = [[] for i in range(n+1)]
v = [False for i in range(n+1)]
inD = [0 for i in range(n+1)]
ans = [0 for i in range(n+1)]
for i in range(m):
    a,b,c = map(int,ip().split())
    arr[a].append([b,c])
    back[b].append([a,c])
    inD[b] += 1
s,e = map(int,ip().split())
cnt = 0
q = [[s,0]]
while q:
    p,x = q.pop(0)
    for i,d in arr[p]:
        inD[i] -= 1
        if i == e:
            cnt += x+1
        ans[i] = max(d+ans[p],ans[i])
        if inD[i] == 0:
            q.append([i,x+1])
print(ans[e])
q.append(e)
cnt = 0
while q:
    p = q.pop(0)
    for nd,di in back[p]:
        if di == ans[p]-ans[nd]:
            cnt += 1
            if not v[nd]:
                v[nd] = True
                q.append(nd)
print(cnt)
