import sys
from collections import deque
ip = sys.stdin.readline
k = int(ip())
w,h = map(int,ip().split())
a = [list(map(int,ip().split())) for i in range(h)]
v = [[[False for i in range(32)] for i in range(w)] for i in range(h)]
dx,dy = (0,1,-1,0),(1,0,0,-1)
hx,hy = (-2,-1,1,2,2,1,-1,-2),(1,2,2,1,-1,-2,-2,-1)
def bfs():
    q = deque()
    q.append((0,0,0,0))
    v[0][0][0] = True
    while q:
        x,y,cnt,c = q.popleft()
        if x == h-1 and y == w-1:
            return cnt
        if c < k:
            for i in range(8):
                nx,ny = x+hx[i],y+hy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if v[nx][ny][c+1] == False and a[nx][ny] != 1:
                        v[nx][ny][c+1] = True
                        q.append((nx,ny,cnt+1,c+1))
        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y
            if 0 <= nx < h and 0 <= ny < w:
                if not(v[nx][ny][c]) and not(a[nx][ny]):
                    v[nx][ny][c] = True
                    q.append([nx,ny,cnt+1,c])
    return -1
print(bfs())
