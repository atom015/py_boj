n = int(input())
arr = []
dp = [[0]*(i+1) for i in range(n)]
for i in range(n):
    arr.append(list(map(int,input().split())))
dp[0][0] = arr[0][0]
for i in range(1,n):
    length = len(arr[i])
    for j in range(length):
        if j == 0:
            dp[i][j] = arr[i][j]+dp[i-1][j]
        elif j == length-1:
            dp[i][j] = arr[i][j]+dp[i-1][j-1]
        elif i != 1 and 0 < j < length-1:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])+arr[i][j]

print(max(dp[n-1]))
