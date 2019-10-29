n,m = map(int,input().split())
a = [list(map(int,input())) for i in range(n)]
dx,dy = [0,0,-1,1],[1,-1,0,0]
v = [[[False,False] for i in range(m)] for i in range(n)]
q = [[0,0,0,0]]
def bfs():
    while len(q) != 0:
        x,y,cnt,chk = q.pop(0)
        if x == n-1 and y == m-1:
            return cnt+1
        for i in range(4):
            nx,ny = dx[i]+x,dy[i]+y
            if 0 <= nx < n and 0 <= ny < m and v[nx][ny][chk] == False:
                v[nx][ny][chk] = True
                if a[nx][ny] == 0:
                    q.append([nx,ny,cnt+1,chk])
                if a[nx][ny] == 1 and chk == 0:
                    q.append([nx,ny,cnt+1,1])
    return -1
print(bfs())
