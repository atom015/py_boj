n,m = map(int,input().split())
arr = [list(input()) for i in range(n)]
chk = [[[[0,0,0,0] for i in range(4)] for i in range(m)] for i in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
q = []
c = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == "S":
            arr[i][j] = "."
            sx,sy = i,j
        if c == False and arr[i][j] == "C":
            arr[i][j] = "D"
            c = True
def checking(a,b):
    if a == b == 1:
        return 3
    elif a == b == 0:
        return 0
    elif a == 1:
        return 1
    elif b == 1:
        return 2
class Tmp:
    def __init__(self,x,y,cnt,dir,cv,dv):
        self.x = x
        self.y = y
        self.cnt = cnt
        self.dir = dir
        self.cv = cv
        self.dv = dv
def bfs(sx,sy):
    q.append(Tmp(sx,sy,0,-1,0,0))
    chk[sx][sy][3][0] = 1
    while q:
        tmp = q.pop(0)
        if tmp.cv and tmp.dv:
            return tmp.cnt
        for i in range(4):
            if i == tmp.dir:continue
            nx,ny = dx[i]+tmp.x,dy[i]+tmp.y
            dc_visit = tmp.cv
            dd_visit = tmp.dv
            if 0 <= nx < n and 0 <= ny < m:
                if chk[nx][ny][i][checking(tmp.cv,tmp.dv)] == 0 and arr[nx][ny] != "#":
                    if arr[nx][ny] == "C":
                        dc_visit = 1
                    if arr[nx][ny] == "D":
                        dd_visit = 1

                    chk[nx][ny][i][checking(dc_visit,dd_visit)] = 1
                    q.append(Tmp(nx,ny,tmp.cnt+1,i,dc_visit,dd_visit))

    return -1
print(bfs(sx,sy))
