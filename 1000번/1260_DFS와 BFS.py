import sys
sys.setrecursionlimit(50000)
def dfs(nd):
    print(nd,end=' ')
    v[nd] = True
    for i in range(1,n+1):
        if v[i] == False and arr[nd][i] == 1:
            dfs(i)
n,m,s = map(int,input().split())
arr = [[0 for i in range(n+1)] for i in range(n+1)]
v = [False for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    arr[a][b] = 1
    arr[b][a] = 1
dfs(s)
print()
q = [s]
v = [False for i in range(n+1)]
v[s] = True
while q:
    p = q.pop(0)
    print(p,end=' ')
    for i in range(1,n+1):
        if v[i] == False and arr[p][i] == 1:
            q.append(i)
            v[i] = True
