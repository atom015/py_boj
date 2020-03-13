from sys import *
setrecursionlimit(5000000)
ip = stdin.readline
def dfs(nd,nc):
    global ans
    c[nd] = nc
    for i in arr[nd]:
        if c[i] == nc:
            ans = False
            return
        if c[i] == 0:
            dfs(i,-nc)
for i in range(int(ip())):
    V,E = map(int,ip().split())
    arr = [[] for i in range(V+1)]
    c = [0 for i in range(V+1)]
    for i in range(E):
        a,b = map(int,ip().split())
        arr[a].append(b)
        arr[b].append(a)
    ans = True
    for i in range(1,V+1):
        if c[i] == 0:
            dfs(i,1)
    if ans == True:
        print("YES")
    else:
        print("NO")
