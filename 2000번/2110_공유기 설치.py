from sys import *
ip = stdin.readline
N,M = map(int,ip().split())
arr = []
for i in range(N):
    arr.append(int(ip()))
arr.sort()
s,e = 0,arr[-1]-arr[0]
def checking(D):
    cnt = 1
    prev = arr[0]
    for i in range(1,N):
        if arr[i]-prev >= D:
            cnt += 1
            prev = arr[i]
    if cnt >= M:
        return 1
while s <= e:
    mid = (s+e)//2
    if checking(mid):
        s = mid+1
    else:
        e = mid-1
print(e)
