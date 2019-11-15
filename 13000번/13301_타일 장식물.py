n = int(input())
if n == 1:
    print(4)
    exit()
dp = [0 for i in range(n)]
dp[0], dp[1] = 1, 1
for i in range(2, n):
    dp[i] = dp[i - 1] + dp[i - 2]
print((max(dp) + (max(dp) + dp[-2])) * 2)
