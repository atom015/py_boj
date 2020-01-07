n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
dp = [[0 for i in range(3)] for i in range(n)]
dp[0] = arr[0]
for i in range(1,n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(arr[i][j]+dp[i-1][1],arr[i][j]+dp[i-1][2])
        elif j == 1:
            dp[i][j] = min(arr[i][j]+dp[i-1][0],arr[i][j]+dp[i-1][2])
        else:
            dp[i][j] = min(arr[i][j]+dp[i-1][0],arr[i][j]+dp[i-1][1])
print(min(dp[n-1]))
