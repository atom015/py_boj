from collections import deque
n,m = map(int,input().split())
arr = [list(input()) for i in range(n)]
vi = [[False for i in range(m)] for i in range(n)]
s,w = 0,0
def bfs(i,j):
    global s,w
    q = deque()
    q.append((i,j))
    vi[i][j] = True
    o,v = 0,0
    while q:
        x,y = q.popleft()
        if arr[x][y] == "o":
            o += 1
        if arr[x][y] == 'v':
            v += 1
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            nx,ny = dx+x,dy+y
            if 0 <= nx < n and 0 <= ny < m:
                if not vi[nx][ny] and arr[nx][ny] != "#":
                    q.append((nx,ny))
                    vi[nx][ny] = True
    if o > v:
        s += o
    else:
        w += v
for i in range(n):
    for j in range(m):
        if not vi[i][j] and arr[i][j] != "#":
            bfs(i,j)
print(s,w)
