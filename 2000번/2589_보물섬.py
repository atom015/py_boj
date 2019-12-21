import sys
ip = sys.stdin.readline
l,w = map(int,ip().split())
arr = [list(ip()) for i in range(l)]
def bfs(x,y):
    v = [[False for i in range(w)] for i in range(l)]
    q = [[x,y,0]]
    v[x][y] = True
    Max = 0
    while q:
        x,y,cnt = q.pop(0)
        Max = max(Max,cnt)
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            nx,ny = dx+x,dy+y
            if 0 <= nx < l and 0 <= ny < w:
                if v[nx][ny] == False and arr[nx][ny] == "L":
                    q.append([nx,ny,cnt+1])
                    v[nx][ny] = True
    return Max
ret = 0
for i in range(l):
    for j in range(w):
        if arr[i][j] == 'L':
            ret = max(ret,bfs(i,j))
print(ret)
