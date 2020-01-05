import sys
ip = sys.stdin.readline
from collections import deque
n,m,h = map(int,ip().split())
arr = []
q = deque([])
v = [[[False]*n for i in range(m)] for i in range(h)]
for _ in range(h):
    tmp = []
    for _ in range(m):
        tmp.append(list(map(int,ip().split())))
    arr.append(tmp)
for i in range(h):
    for j in range(m):
        for k in range(n):
            if arr[i][j][k] == 1:
                q.append([i,j,k,0])
                v[i][j][k] = True
            if arr[i][j][k] == -1:
                v[i][j][k] = True
def checking():
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if v[i][j][k] == 0:
                    return False
    return True
def bfs():
    while q:
        x,y,z,cnt = q.popleft()
        for dx,dy,dz in (0,0,-1),(0,0,1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0):
            nx,ny,nz = x+dx,y+dy,z+dz
            if 0 <= nx < h and 0 <= ny < m and 0 <= nz < n:
                if v[nx][ny][nz] == False and arr[nx][ny][nz] != -1:
                    q.append([nx,ny,nz,cnt+1])
                    v[nx][ny][nz] = True
    if not checking():
        return -1
    return cnt
print(bfs())
