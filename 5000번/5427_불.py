from collections import deque
def bfs(v,q,sx,sy):
    q.append((sx,sy,0,0))
    v[sx][sy] = True
    dx,dy = [0,0,-1,1],[1,-1,0,0]
    while q:
        x,y,cnt,chk = q.popleft()
        if chk == 1:
            for i in range(4):
                nx,ny = dx[i]+x,dy[i]+y
                if 0 <= nx < c and 0 <= ny < r:
                    if not(v[nx][ny]) and a[nx][ny] != "#":
                        q.append((nx,ny,0,1))
                        v[nx][ny] = True
        else:
            for i in range(4):
                nx,ny = dx[i]+x,dy[i]+y
                if 0 <= nx < c and 0 <= ny < r:
                    if not(v[nx][ny]) and a[nx][ny] != "#":
                        q.append((nx,ny,cnt+1,0))
                        v[nx][ny] = True
                else:
                    return cnt+1
    return "IMPOSSIBLE"
for i in range(int(input())):
    r,c = map(int,input().split())
    a = [list(input()) for i in range(c)]
    v = [[False for i in range(r)] for i in range(c)]
    q = deque([])
    for i in range(c):
        for j in range(r):
            if a[i][j] == "@":
                sx,sy = i,j
            if a[i][j] == "*":
                q.append((i,j,0,1))
                v[i][j] = True
    print(bfs(v,q,sx,sy))
