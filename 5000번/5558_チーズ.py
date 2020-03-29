from collections import deque
from sys import *
ip = stdin.readline
n,m,c = map(int,ip().split())
arr = [list(ip().strip()) for i in range(n)]
chk,ret = 1,0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "S":
            mx,my = i,j
def bfs(v):
    global chk,ret,mx,my
    q = deque([])
    q.append((mx,my,0))
    v[mx][my] = True
    while q:
        x,y,cnt = q.popleft()
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            nx,ny = dx+x,dy+y
            if 0 <= nx < n and 0 <= ny < m and not v[nx][ny] and arr[nx][ny] != "X":
                if arr[nx][ny] in "123456789" and chk >= int(arr[nx][ny]):
                    chk += 1
                    mx,my = nx,ny
                    arr[nx][ny] = "."
                    ret += cnt+1
                    return
                q.append([nx,ny,cnt+1])
                v[nx][ny] = True
for i in range(c):
    v = [[False]*m for i in range(n)]
    bfs(v)
print(ret)
