from sys import *
setrecursionlimit(10**9)
ip = stdin.readline
n = int(ip())
arr = [[] for i in range(n+1)]
for i in range(n-1):
    a,b,c = map(int,ip().split())
    arr[a].append([b,c])
    arr[b].append([a,c])
v = [False for i in range(n+1)]
def dfs(nd,cost):
    global d,node
    v[nd] = True
    if cost > d:
        node,d = nd,cost
    for i,dist in arr[nd]:
        if not v[i]:
            dfs(i,cost+dist)
d,node = 0,0
dfs(1,0)
v = [False for i in range(n+1)]
d = 0
dfs(node,0)
print(d)
