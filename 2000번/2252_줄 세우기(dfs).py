import sys
sys.setrecursionlimit(10**6)
ip = sys.stdin.readline
n,m = map(int,ip().split())
arr = [[] for _ in range(n+1)]
v = [False for _ in range(n+1)]
ans = []
def dfs(nd):
    if v[nd]:return
    v[nd] = True
    for i in arr[nd]:
        if v[i] == False:
            dfs(i)
    ans.append(nd)
for i in range(m):
    a,b = map(int,ip().split())
    arr[b].append(a)
for i in range(1,n+1):
    if v[i] == False:
        dfs(i)
print(*ans)
