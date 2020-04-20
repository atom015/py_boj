import sys
from heapq import *
ip = sys.stdin.readline
n,m,k = map(int,ip().strip().split())
adj = [[] for i in range(n)]
for i in range(m):
    a,b,c = map(int,ip().strip().split())
    adj[a-1].append((b-1,c))

d = [[] for i in range(n)]
def dijkstra():
    q = [[0,0]]
    heappush(d[0],0)
    while q:
        dist,nd = heappop(q)
        for p,cost in adj[nd]:
            cost += dist
            if len(d[p]) < k:
                heappush(d[p],-cost)
                heappush(q,(cost,p))
            elif d[p][0] < -cost:
                heappop(d[p])
                heappush(d[p],-cost)
                heappush(q,(cost,p))
dijkstra()

for i in d:
    print(-i[0] if len(i) == k else -1)
