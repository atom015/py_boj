from collections import deque
r,c = map(int,input().split())
a = [list(input()) for i in range(r)]
v = [[False for i in range(c)] for i in range(r)]
dx,dy = (1,-1,0,0),(0,0,-1,1)
q = deque([])
for i in range(r):
    for j in range(c):
        if a[i][j] == "F":
            q.append((i,j,0,1))
            v[i][j] = True
        if a[i][j] == "J":
            sx,sy = i,j
def bfs(sx,sy):
    q.append((sx,sy,0,0))
    v[sx][sy] = True
    while q:
        x,y,cnt,chk = q.popleft()
        if chk == 1:
            for i in range(4):
                nx,ny = dx[i]+x,dy[i]+y
                if 0 <= nx < r and 0 <= ny < c:
                    if a[nx][ny] != "#" and v[nx][ny] != True:
                        q.append((nx,ny,0,1))
                        v[nx][ny] = True
        else:
            for i in range(4):
                nx,ny = dx[i]+x,dy[i]+y
                if 0 <= nx < r and 0 <= ny < c:
                    if a[nx][ny] != "#" and v[nx][ny] != True:
                        q.append((nx,ny,cnt+1,0))
                        v[nx][ny] = True
                else:
                    return cnt+1
    return "IMPOSSIBLE"
print(bfs(sx,sy))
