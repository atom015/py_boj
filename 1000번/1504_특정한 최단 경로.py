import queue as Q
import sys
ip = sys.stdin.readline
v,e = map(int, ip().split())

adj = [[] for i in range (v+1)]
for i in range(e):
    a, b, c = map(int,ip().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
s,e = map(int,input().split())

def dijkstra(s,p):
    d = [1e9]*(v+1)
    q = Q.PriorityQueue()
    q.put((0, s))
    d[s] = 0
    while not q.empty():
        pp = q.get()
        here = pp[1]
        dist = pp[0]
        if d[here] < dist:
            continue
        for i in adj[here]:
            cost = dist + i[1]
            if d[i[0]] > cost:
                d[i[0]] = cost
                q.put((cost, i[0]))
    return d[p]
ans = min(dijkstra(1,s)+dijkstra(s,e)+dijkstra(e,v),dijkstra(1,e)+dijkstra(e,s)+dijkstra(s,v))
if 0 < ans < 1e9:
    print(ans)
else:
    print(-1)
