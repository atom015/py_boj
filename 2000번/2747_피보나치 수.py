n = int(input())
dp = [0 for i in range(n+1)]
dp[0] = 0
dp[1] = 1
def fibo(n):
    if n <= 1:
        return dp[n]
    else:
        if dp[n] > 0:
            return dp[n]
        else:
            dp[n] = fibo(n-1) + fibo(n-2)
            return dp[n]
print(fibo(n))
