from sys import *
from heapq import *
ip = stdin.readline
n,k = map(int,ip().split())
PQ = []
arr,arr2 = [],[]
for i in range(k):
    heappush(PQ,[0,i])
for i in range(n):
    a,b = map(int,ip().split())
    p = heappop(PQ)
    heappush(PQ,[p[0]+b,p[1]])
    arr.append([p[0]+b,p[1],i+1])
    arr2.append(a)
arr.sort(key=lambda x:[x[0],-x[1]])
s = 0
for i in range(n):
    s += arr2[arr[i][2]-1]*(i+1)
print(s)
