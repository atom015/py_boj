n,m = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = 2

def check(x,y):
    cnt = 0
    for dx,dy in (0,1),(1,0),(-1,0),(0,-1):
        nx,ny = dx+x,dy+y
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 1:
                cnt += 1
    if cnt >= 2:
        return False
    return True
def air():
    v = [[False for i in range(m)] for i in range(n)]
    v[0][0] = True
    arr[0][0] = 1
    q = [[0,0]]
    while q:
        x,y = q.pop(0)
        for dx,dy in (0,1),(1,0),(-1,0),(0,-1):
            nx,ny = dx+x,dy+y
            if 0 <= nx < n and 0 <= ny < m:
                if v[nx][ny] == False:
                    if arr[nx][ny] == 1 or arr[nx][ny] == 0:
                        q.append([nx,ny])
                        arr[nx][ny] = 1
                        v[nx][ny] = True
air()
def all_zero():
    for i in arr:
        for j in i:
            if j == 2:
                return False
    return True
def func():
    cnt = 0
    while not all_zero():
        air()
        q = []
        for i in range(n):
            for j in range(m):
                if not check(i,j):
                    q.append([i,j])
        while q:
            x,y = q.pop(0)
            arr[x][y] = 1
        cnt += 1
    return cnt
print(func())
