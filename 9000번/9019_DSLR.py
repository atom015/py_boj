import sys
from collections import deque
ip = sys.stdin.readline
def bfs(a,b):
    v = [False for i in range(10001)]
    q = deque([(a,"")])
    v[a] = True
    while q:
        p,chk = q.popleft()
        if p == int(b):
            return chk

        tp = (2*p) % 10000
        if not(v[tp]):
            q.append((tp,chk+"D"))
            v[tp] = True

        tp = p-1 if p != 0 else 9999
        if not(v[tp]):
            q.append((tp,chk+"S"))
            v[tp] = True

        tp = (p % 1000) * 10 + p // 1000
        if not(v[tp]):
            q.append((tp,chk+"L"))
            v[tp] = True

        tp = (p % 10) * 1000 + (p // 10)
        if not(v[tp]):
            q.append((tp,chk+"R"))
            v[tp] = True
for i in range(int(ip())):
    a,b = map(int,ip().split())
    print(bfs(a,b))
