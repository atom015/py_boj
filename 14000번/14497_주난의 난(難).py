n,m = map(int,input().split())
sx,sy,ex,ey = map(int,input().split())
sx,sy = sx-1,sy-1
arr = [list(input()) for i in range(n)]
def bfs():
    q = [[sx,sy]]
    while q:
        x,y = q.pop(0)
        for dx,dy in (1,0),(0,1),(0,-1),(-1,0):
            nx,ny = dx+x,dy+y
            if 0 <= nx < n and 0 <= ny < m:
                if v[nx][ny] == False:
                    v[nx][ny] = True
                    if arr[nx][ny] == '1':
                        arr[nx][ny] = '0'
                    elif arr[nx][ny] == "#":
                        return True
                    else:
                        q.append([nx,ny])
ans = 0
while 1:
    ans += 1
    v = [[False for i in range(m)] for i in range(n)]
    a = bfs()
    if a:break
print(ans)
