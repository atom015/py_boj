import sys
sys.setrecursionlimit(500000000)
ip = sys.stdin.readline
n,s,e = map(int,ip().split())
arr = [[] for i in range(100000+1)]
v = [False for i in range(100000+1)]
ans = 0
def dfs(nd,S,ma):
    global ans
    if nd == e:
        ans = S-ma
        return
    v[nd] = True
    for node,dist in arr[nd]:
        if not v[node]:
            if ma > dist:
                dfs(node,S+dist,ma)
            else:
                dfs(node,S+dist,dist)
for i in range(n-1):
    a,b,c = map(int,ip().split())
    arr[a].append([b,c])
    arr[b].append([a,c])
dfs(s,0,0)
print(ans)
