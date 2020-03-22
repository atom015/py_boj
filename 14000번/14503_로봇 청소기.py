n,m = map(int,input().split())
sx,sy,sw = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
dx,dy = [-1,0,1,0],[0,1,0,-1]
dx1,dy1 = [1,0,-1,0],[0,-1,0,1]
cnt = 0
def left(n):
    if n == 0:
        return 3
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return 2
q = [[sx,sy,sw]]
while q:
    x,y,w = q.pop(0)
    if arr[x][y] == 0:
        arr[x][y] = 2
        cnt += 1
    nw,chk = w,False
    for i in range(4):
        nw = left(nw)
        nx,ny = dx[nw]+x,y+dy[nw]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 0:
                q.append([nx,ny,nw])
                chk = True
                break
    if not chk:
        nx,ny = x+dx1[w],y+dy1[w]
        if arr[nx][ny] != 1:
            q.append([nx,ny,w])

print(cnt)
