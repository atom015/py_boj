from collections import deque
import sys
ip = sys.stdin.readline
n,m = map(int,ip().split())
arr = [list(map(int,ip().split())) for i in range(n)]
v = [[[0,0,0,0] for i in range(m)] for i in range(n)]
sx,sy,sw = map(int,ip().split())
ex,ey,ew = map(int,ip().split())
q = deque([[sx-1,sy-1,sw-1,0]])
v[sx-1][sy-1][sw-1] = 1
dx,dy = [0,0,1,-1],[1,-1,0,0]
def bfs():
    while q:
        x,y,way,cnt = q.popleft()
        if x == ex-1 and y == ey-1 and way == ew-1:
            return cnt
        for i in range(1,4):
            nx,ny = x+dx[way]*i,y+dy[way]*i
            if 0 <= nx < n and 0 <= ny < m and not arr[nx][ny]:
                if not v[nx][ny][way]:
                    q.append([nx,ny,way,cnt+1])
                    v[nx][ny][way] = 1
            else:break
        if way == 0 or way == 1:
            nx,ny = 2,3
        if way == 2 or way == 3:
            nx,ny = 0,1
        if v[x][y][nx] == 0:
            v[x][y][nx] = 1
            q.append([x,y,nx,cnt+1])
        if v[x][y][ny] == 0:
            v[x][y][ny] = 1
            q.append([x,y,ny,cnt+1])


print(bfs())
