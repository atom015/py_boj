from sys import *
ip = stdin.readline
def getP(x):
    if p[x] == x:
        return x
    p[x] = getP(p[x])
    return p[x]
def union(a,b):
    a = getP(a)
    b = getP(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b
N,Q = map(int,ip().split())
arr = []
p = [i for i in range(N+1)]
for i in range(N):
    x1,x2,y = map(int,ip().split())
    arr.append([x1,x2,i])
arr.sort()
for i in range(1,N):
    if arr[i][0] <= arr[i-1][1]:
        union(arr[i-1][2]+1,arr[i][2]+1)
        arr[i][1] = max(arr[i-1][1],arr[i][1])
for i in range(Q):
    a,b = map(int,ip().split())
    if getP(a) == getP(b):
        print(1)
    else:
        print(0)
