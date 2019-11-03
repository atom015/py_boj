n = int(input())
arr = [[] for i in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
v = [False for i in range(n+1)]
p = [0 for i in range(n+1)]
for i in range(len(arr)):
    arr[i] = sorted(arr[i])
def dfs(nd,n):
    v[nd] = True
    for i in range(len(arr[nd])):
        if v[arr[nd][i]] == False:
            p[arr[nd][i]] = nd
            dfs(arr[nd][i],n)
dfs(1,n)
for i in range(2,n+1):
    print(p[i])
