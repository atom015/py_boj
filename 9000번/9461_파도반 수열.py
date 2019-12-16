def main(n):
    if 1 <= n <= 3:
        return 1
    dp = [0]+[0 for i in range(n+1)]
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4,n+1):
        dp[i] = dp[i-2]+dp[i-3]
    return dp[n]

for i in range(int(input())):
    print(main(int(input())))
