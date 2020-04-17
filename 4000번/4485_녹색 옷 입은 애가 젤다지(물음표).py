from heapq import *
from sys import *
ip = stdin.readline
cnt = 1
def bfs():
    q = [[0,0,arr[0][0]]]
    dx,dy = [0,0,1,-1],[-1,1,0,0]
    while q:
        x,y,cost = heappop(q)
        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y
            if 0 <= nx < n and 0 <= ny < n:
                if arr2[nx][ny] > cost+arr[nx][ny]:
                    heappush(q,[nx,ny,cost+arr[nx][ny]])
                    arr2[nx][ny] = cost+arr[nx][ny]
    return arr2[n-1][n-1]
while 1:
    n = int(ip())
    if n == 0:break
    arr = [list(map(int,ip().split())) for i in range(n)]
    arr2 = [[1e9 for i in range(n)] for i in range(n)]
    print("Problem {}: {}".format(cnt,bfs()))
    cnt += 1
