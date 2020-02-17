n,m,t = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n)]
v = [[[False,False] for i in range(m)] for i in range(n)]
def bfs():
    q = [[0,0,0,0]]
    v[0][0][0] = True
    while q:
        x,y,cnt,chk = q.pop(0)
        if x == n-1 and y == m-1 and cnt <= t:
            return cnt
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            nx,ny = dx+x,dy+y
            if 0 <= nx < n and 0 <= ny < m:
                if v[nx][ny][chk] == False:
                    if arr[nx][ny] == 1 and chk == 1:
                        q.append([nx,ny,cnt+1,chk])
                        v[nx][ny][chk] = True
                    elif arr[nx][ny] == 0:
                        q.append([nx,ny,cnt+1,chk])
                        v[nx][ny][chk] = True
                    elif arr[nx][ny] == 2:
                        q.append([nx,ny,cnt+1,1])
                        v[nx][ny][chk] = True

    return "Fail"
print(bfs())
