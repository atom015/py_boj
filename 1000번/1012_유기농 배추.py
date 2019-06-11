import sys
sys.setrecursionlimit(50000) #재귀 재한 깊이를 50000으로설정
def dfs(x,y):
    li[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and li[nx][ny] == 1:
            dfs(nx,ny)
dx = [1,0,-1,0]
dy = [0,-1,0,1]
for i in range(int(input())):
    m,n,k = map(int,input().split()) #M:가로길이,N:세로길이,K:위치개수
    li = [[0 for i in range(m)] for i in range(n)]
    for i in range(k):
        a,b = map(int,input().split())
        li[b][a] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if li[i][j] == 1:
                dfs(i,j)
                cnt += 1
    print(cnt)
