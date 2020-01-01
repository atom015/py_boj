from collections import deque
import sys
sys.setrecursionlimit(500000000)
ip = sys.stdin.readline
n = int(ip())
arr = [list(map(int,ip().split())) for i in range(n)]
def dfs(x,y,v,cnt):
    arr[x][y] = cnt
    v[x][y] = True
    for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
        nx,ny = dx+x,dy+y
        if 0 <= nx < n and 0 <= ny < n:
            if v[nx][ny] != True and arr[nx][ny]:
                dfs(nx,ny,v,cnt)
def island_chk():
    v = [[False for i in range(n)] for i in range(n)]
    cnt = 1
    for i in range(n):
        for j in range(n):
            if arr[i][j] and v[i][j] != True:
                dfs(i,j,v,cnt)
                cnt += 1
    return cnt
def bfs(cnt):
    v = [[False for i in range(n)] for i in range(n)]
    q = deque([])
    for i in range(n):
        for j in range(n):
            if arr[i][j] == cnt:
                v[i][j] = True
                q.append([i,j])
    ret = 0
    while q:
        for i in range(len(q)):
            x,y = q.popleft()
            for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
                nx,ny = dx+x,dy+y
                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] != cnt and arr[nx][ny]:
                        return ret
                    if arr[nx][ny] == 0 and v[nx][ny] == False:
                        q.append([nx,ny])
                        v[nx][ny] = True
        ret += 1

cnt = island_chk()
ret = 1000000000000
for i in range(1,cnt):
    ret = min(ret,bfs(i))
print(ret)
