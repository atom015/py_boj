import sys
sys.setrecursionlimit(50000)
n,m = map(int,sys.stdin.readline().split())
li = [[] for i in range(n+1)]
chk = [False for i in range(n+1)]
for i in range(m):
    u,v = map(int, sys.stdin.readline().split())
    li[u].append(v)
    li[v].append(u)

def dfs(nd):
    chk[nd] = True
    for i in li[nd]:
        if chk[i] is False:
            dfs(i)
cnt = 0
for i in range(1,n+1):
    if chk[i] is False:
        dfs(i)
        cnt += 1
print(cnt)
