from sys import *
setrecursionlimit(10**9)
ip = stdin.readline
n,m = map(int,ip().split())
graph = [[] for i in range(n+1)]
arr = [0]+list(map(int,ip().split()))
co = [0]*(n+1)
for i in range(2,n+1):
    graph[arr[i]].append(i)
def dfs(nd):
    for i in graph[nd]:
        co[i] += co[nd]
        dfs(i)
for _ in range(m):
    i,w = map(int,ip().split())
    co[i] += w
dfs(1)
for i in range(1,n+1):
    print(co[i],end=' ')
