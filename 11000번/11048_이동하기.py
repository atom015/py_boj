from sys import *
ip = stdin.readline
n,m = map(int,ip().split())
dp = [[0 for i in range(m)] for i in range(n)]
arr = [list(map(int,ip().split())) for i in range(n)]
dp[0][0] = arr[0][0]
for i in range(n):
    for j in range(m):
        for dx,dy in (0,1),(1,0),(1,1):
            nx,ny = dx+i,dy+j
            if nx < n and ny < m:
                dp[nx][ny] = max(dp[i][j]+arr[nx][ny],dp[nx][ny])
print(dp[n-1][m-1])
