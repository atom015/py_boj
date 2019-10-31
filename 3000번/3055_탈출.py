r,c = map(int,input().split())
a = [list(input()) for i in range(r)]
v = [[False for i in range(c)] for i in range(r)]
dx,dy = [1,-1,0,0],[0,0,1,-1]
q = []
def s():
    for i in range(r):
        for j in range(c):
            if a[i][j] == "*":
                q.append([i,j,0,1])
            if a[i][j] == "S":
                sx,sy = i,j
    return sx,sy
sx,sy = s()
def bfs(sx,sy):
    q.append([sx,sy,0,0])
    v[sx][sy] = True
    while q:
        x,y,cnt,chk = q.pop(0)
        if chk == 1:
            for i in range(4):
                nx,ny = dx[i]+x,dy[i]+y
                if 0 <= nx < r and 0 <= ny < c:
                    if v[nx][ny] != True and a[nx][ny] != "X" and a[nx][ny] != "D":
                        q.append([nx,ny,0,chk])
                        v[nx][ny] = True
        else:
            if a[x][y] == "D":
                return cnt
            for i in range(4):
                nx,ny = dx[i]+x,dy[i]+y
                if 0 <= nx < r and 0 <= ny < c:
                    if v[nx][ny] != True and a[nx][ny] != "X":
                        q.append([nx,ny,cnt+1,chk])
                        v[nx][ny] = True
    return "KAKTUS"
print(bfs(sx,sy))
