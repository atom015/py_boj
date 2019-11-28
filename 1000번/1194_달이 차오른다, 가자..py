import sys
ip = sys.stdin.readline
n,m = map(int,ip().split()) #가로, 세로
arr = [list(ip()) for i in range(n)]
v = [[[False for _ in range(64)] for _ in range(50)] for _ in range(50)]
def bfs(x,y):
    q = [[x,y,0,0]]
    v[x][y][0] = True
    while q:
        x,y,cnt,key = q.pop(0)
        if arr[x][y] == "1":
            return cnt
        for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
            nx,ny = dx+x,dy+y
            if 0 <= nx < n and 0 <= ny < m:
                if not(v[nx][ny][key]):
                    if arr[nx][ny] == "." or arr[nx][ny] == "1":
                        v[nx][ny][key] = True
                        q.append([nx,ny,cnt+1,key])

                    elif "a" <= arr[nx][ny] <= "f":
                        tmp_key = key | (1 << (ord(arr[nx][ny])-ord("a")))
                        q.append([nx,ny,cnt+1,tmp_key])
                        v[nx][ny][tmp_key] = True

                    elif "A" <= arr[nx][ny] <= "F":
                        Door = key & (1 << (ord(arr[nx][ny]) - ord("A")))
                        if Door:
                            v[nx][ny][key] = True
                            q.append([nx,ny,cnt+1,key])


    return -1
for i in range(n):
    for j in range(m):
        if arr[i][j] == "0":
            arr[i][j] = "."
            sx,sy = i,j
print(bfs(sx,sy))
