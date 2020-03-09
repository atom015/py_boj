n,m = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = 2
def check(x,y):
    cnt = 0
    q = [[x,y]]
    while q:
        x,y = q.pop(0)
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            nx,ny = dx+x,dy+y
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    cnt += 1
    if cnt >= 1:
        return False
    return True
def cheeze_cnt():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                cnt += 1
    return cnt
def bfs1():
    v = [[False for i in range(m)] for i in range(n)]
    q = [[0,0]]
    arr[0][0] = 1
    v[0][0] = True
    while q:
        x,y = q.pop(0)
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            nx,ny = dx+x,dy+y
            if 0 <= nx < n and 0 <= ny < m:
                if v[nx][ny] == False:
                    if arr[nx][ny] == 1 or arr[nx][ny] == 0:
                        q.append([nx,ny])
                        v[nx][ny] = True
                        arr[nx][ny] = 1
bfs1()
def all_check(arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 1:
                return False
    return True
def func():
    global ans
    cnt = 0
    while all_check(arr) == False:
        ans = cheeze_cnt()
        q = []
        for i in range(n):
            for j in range(m):
                if not check(i,j):
                    q.append([i,j])
        while q:
            x,y = q.pop(0)
            arr[x][y] = 1
        bfs1()
        cnt += 1
    return cnt
ret = func()
print(ret)
print(ans)
