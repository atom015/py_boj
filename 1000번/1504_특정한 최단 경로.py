import queue as Q
import sys
ip = sys.stdin.readline
v,e = map(int, ip().split())

adj = [[] for i in range (v+1)]
ans = [1e9]*(v+1)
for i in range(e):
    a, b, c = map(int,ip().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
s,e = map(int,input().split())

def dijkstra(s):
    q = Q.PriorityQueue()
    q.put((0, s))
    ans[s] = 0
    while not q.empty():
        pp = q.get()
        here = pp[1]
        dist = pp[0]
        if ans[here] < dist:
            continue
        for i in adj[here]:
            cost = dist + i[1]
            if ans[i[0]] > cost:
                ans[i[0]] = cost
                q.put((cost, i[0]))
dijkstra(1)
ans1 = ans[s]
ans2 = ans[e]
ans = [1e9]*(v+1)
if ans1 == 1e9 and ans2 == 1e9:
    print(-1)
else:
    dijkstra(s)
    ans1 += ans[e]
    ans2 += ans[e]
    ans = [1e9]*(v+1)
    dijkstra(e)
    ans1 += ans[v]
    ans = [1e9]*(v+1)
    dijkstra(s)
    ans2 += ans[v]
    print(min(ans1,ans2))
