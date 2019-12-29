from collections import deque
import sys
ip = sys.stdin.readline
n,m,k = map(int,ip().split())
a = [list(ip()) for i in range(n)]
v = [[[0]*(k+1) for i in range(m)] for i in range(n)]
q = deque([[0,0,0,0]])
def bfs():
    while q:
        x,y,cnt,chk = q.popleft()
        if x == n-1 and y == m-1:
            return cnt+1
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            nx,ny = dx+x,dy+y
            if 0 <= nx < n and 0 <= ny < m:
                if v[nx][ny][chk] == False:
                    v[nx][ny][chk] = 1
                    if a[nx][ny] == '0':
                        q.append([nx,ny,cnt+1,chk])
                    if a[nx][ny] == '1' and chk < k:
                        q.append([nx,ny,cnt+1,chk+1])

    return -1
print(bfs())
