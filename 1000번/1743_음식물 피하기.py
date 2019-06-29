import sys
sys.setrecursionlimit(50000)
n,m,k = map(int,input().split())
li = [[0 for i in range(m)] for i in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
compare = 0
for i in range(k):
    a,b = map(int,input().split())
    li[a-1][b-1] = 1
def dfs(x,y):
    global cnt
    cnt += 1
    li[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if li[nx][ny] == 1:
                dfs(nx,ny)
    return cnt
for i in range(n):
    for j in range(m):
        if li[i][j] == 1:
            cnt = 0
            func = dfs(i,j)
            if compare < func:
                compare = func
print(compare)
