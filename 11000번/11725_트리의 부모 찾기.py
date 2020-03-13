from sys import *
setrecursionlimit(50000000)
ip = stdin.readline
def dfs(nd):
    v[nd] = True
    for i in arr[nd]:
        if v[i] == False:
            ans[i] = nd
            dfs(i)
n = int(ip())
ans = [0 for i in range(n)]
arr = [[] for i in range(n)]
v = [False for i in range(n)]
for i in range(n-1):
    a,b = map(int,ip().split())
    arr[a-1].append(b-1)
    arr[b-1].append(a-1)
dfs(0)
for i in range(1,n):
    print(ans[i]+1)
