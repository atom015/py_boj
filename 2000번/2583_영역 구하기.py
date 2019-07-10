import sys
sys.setrecursionlimit(50000)
m,n,k = map(int,input().split()) #세로,가로
dx = [1,0,-1,0]
dy = [0,-1,0,1]
li = [[0 for i in range(n)] for i in range(m)]
visited = [[False for i in range(n)] for i in range(m)]
result = []
for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for y in range((m-y2),(m-y1),1):
        for x in range(x1,x2,1):
            li[y][x] = 1
            visited[y][x] == True
def dfs(x,y):
    global cnt
    cnt += 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if li[nx][ny] == 0 and visited[nx][ny] == False:
                dfs(nx,ny)
    return cnt
for i in range(m):
    for j in range(n):
        if li[i][j] == 0 and visited[i][j] == False:
            cnt = 0
            result.append(dfs(i,j))
print(len(result))
for i in sorted(result):
    print(i,end=' ')
