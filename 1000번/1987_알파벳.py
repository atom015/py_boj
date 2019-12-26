import sys
ip = sys.stdin.readline
r,c = map(int,ip().split())
arr = [list(ip()) for i in range(r)]
ret = -1
def dfs(x,y,al,cnt):
    global ret
    al = al | (1 << (ord(arr[x][y])-ord('A')))
    for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
        nx,ny = dx+x,dy+y
        if 0 <= nx < r and 0 <= ny < c:
            if not (al & (1 << (ord(arr[nx][ny]) - ord('A')))):
                dfs(nx,ny,al,cnt+1)
    ret = max(ret,cnt)
dfs(0,0,1<<26,1)
print(ret)
