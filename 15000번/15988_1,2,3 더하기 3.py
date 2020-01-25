dp = [0 for i in range(1000001)]
dp[0],dp[1],dp[2] = 1,2,4
for i in range(3,1000001):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3]) % 1000000009
for i in range(int(input())):
    n = int(input())
    print(dp[n-1]%1000000009)
