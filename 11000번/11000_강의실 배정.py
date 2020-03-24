from heapq import *
import sys
ip = sys.stdin.readline
n = int(ip())
arr = []
for i in range(n):
    a,b = map(int,ip().split())
    arr.append([a,b])
arr.sort()
q = []
heappush(q,arr[0][1])
for i in range(1,n):
    if q[0] <= arr[i][0]:
        heappop(q)
        heappush(q,arr[i][1])
    else:
        heappush(q,arr[i][1])
print(len(q))
