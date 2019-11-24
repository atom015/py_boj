import sys
import queue as Q
ip = sys.stdin.readline
n,m = map(int,ip().split())
inf = 1e9
d = [inf]*(n+1)
adj = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,ip().split())
    adj[a].append([b,1])
    adj[b].append([a,1])
def dijkstra(s):
    q = Q.PriorityQueue()
    q.put((0,s))
    d[s] = 0
    while not q.empty():
        dist,nd = q.get()
        if d[nd] < dist:
            continue
        for i in adj[nd]:
            cost = dist+i[1]
            if d[i[0]] > cost:
                d[i[0]] = cost
                q.put((cost,i[0]))
dijkstra(1)
MAX = max(d[1:])
for i in range(n):
    if d[i] == MAX:
        print(i,end=' ')
        break
print(MAX,d.count(MAX))
