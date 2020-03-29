from heapq import *
from sys import *
ip = stdin.readline
N = int(ip())
q = []
cnt = 0
for i in range(N):
    heappush(q,int(ip()))
while len(q) != 1:
    if len(q) >= 2:
        p = heappop(q)
        p1 = heappop(q)
        cnt += p+p1
        heappush(q,p+p1)
print(cnt)
