n = int(input())
dp = [0 for i in range(1000001)]
dp[0],dp[1] = 1,2
for i in range(2,n):
    dp[i] = (dp[i-1]+dp[i-2])%15746
print(dp[n-1]%15746)
