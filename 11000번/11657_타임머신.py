import sys
ip = sys.stdin.readline
class Node:
    def __init__(self,u,v,w):
        self.u = u
        self.v = v
        self.w = w

V,E = map(int,ip().split())
inf = 1000000000
arr = [0 for i in range(E+1)]
d = [inf for i in range(V+1)]
for i in range(1,E+1):
    a,b,c = map(int,ip().split())
    arr[i] = Node(a,b,c)

d[1] = 0
chk = False
for i in range(1,V):
    for j in range(1,E+1):
        u,v,w = arr[j].u,arr[j].v,arr[j].w
        if d[u] != inf:
            d[v] = min(d[v],d[u]+w)
for i in range(1,E+1):
    u,v,w = arr[i].u,arr[i].v,arr[i].w
    if d[u] != inf and d[v] > d[u]+w:
        chk = True
        break
if chk:
    print(-1)
else:
    for i in range(2,V+1):
        print(d[i] if d[i] != inf else -1)
