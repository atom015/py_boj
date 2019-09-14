import sys
sys.setrecursionlimit(5000000)
n,m = map(int,input().split())
a = [list(map(int,input().split())) for i in range(n)]
chk = [[False for i in range(m)] for i in range(n)]
ans = 0
cnt = 0
dx = [1,-1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    global com
    com += 1
    chk[x][y] = True
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 1 and chk[nx][ny] == False:
                dfs(nx,ny)
for i in range(n):
    for j in range(m):
        if a[i][j] == 1 and chk[i][j] == False:
            cnt += 1
            com = 0
            dfs(i,j)
            ans = max(ans,com)
print(cnt)
print(ans)
