import sys
sys.setrecursionlimit(50000)
def dfs(nd):
    print(nd,end=' ')
    v[nd] = True
    for i in arr[nd]:
        if v[i] == False:
            dfs(i)
n,m,s = map(int,input().split())
arr = [[] for i in range(n+1)]
v = [False for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
    arr[a].sort()
    arr[b].sort()
dfs(s)
print()
v = [False for i in range(n+1)]
v[s] = True
q = [s]
while q:
    p = q.pop(0)
    print(p,end=' ')
    for i in arr[p]:
        if v[i] == False:
            q.append(i)
            v[i] = True
