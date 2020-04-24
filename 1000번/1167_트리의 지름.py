from sys import *
setrecursionlimit(10**9)
ip = stdin.readline
n = int(ip())
arr = [[] for i in range(n+1)]
for i in range(n):
    li = list(map(int,ip().split()))
    li.pop()
    a = li.pop(0)
    for i in range(0,len(li),2):
        arr[a].append([li[i],li[i+1]])
def dfs(nd,cost):
    global d,node
    v[nd] = 1
    if cost > d:
        d,node = cost,nd
    for i,dist in arr[nd]:
        if not v[i]:
            dfs(i,cost+dist)
d,node = 0,0
v = [0]*(n+1)
dfs(1,0)
v = [0]*(n+1)
d = 0
dfs(node,0)
print(d)
