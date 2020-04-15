from sys import *
setrecursionlimit(10**9)
ip = stdin.readline
def find(p,x):
    if x == p[x]:
        return x
    p[x] = find(p,p[x])
    return p[x]
def up(p,a,b):
    a = find(p,a)
    b = find(p,b)
    if a == b: return 0
    p[a] = b
    return 1
def dfs(nd,cost):
    v[nd] = 1
    d[nd] = cost
    for i,dist in arr[nd]:
        if v[i] == 1:continue
        v[i] = 1
        dfs(i,cost+dist)
while 1:
    n,m = map(int,ip().split())
    if n == m == 0:break
    p = [i for i in range(n+1)]
    d = [0 for i in range(n+1)]
    arr = [[] for i in range(n+1)]
    v = [0 for i in range(n+1)]
    im = [0 for i in range(100000+1)]
    q = []
    for i in range(1,m+1):
        li = ip().strip().split()
        if li[0] == "!":
            a,b,c = list(map(int,li[1:]))
            up(p,a,b)
            arr[a].append([b,c])
            arr[b].append([a,-c])
        else:
            a,b = list(map(int,li[1:]))
            q.append([a,b])
            if find(p,a) != find(p,b):
                im[len(q)-1] = 1
    for i in range(1,n+1):
        if not v[i]:
            dfs(i,0)
    for i in range(len(q)):
        s,e = q[i]
        if im[i]:
            print("UNKNOWN")
        else:
            print(d[e]-d[s])
