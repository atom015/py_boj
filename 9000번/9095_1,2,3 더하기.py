t = int(input())
for i in range(t):
    dp = [0 for i in range(15)]
    dp[0],dp[1],dp[2] = 1,1,2
    k = int(input())
    for i in range(3,k+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    print(dp[k])
