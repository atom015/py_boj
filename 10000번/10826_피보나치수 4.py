import sys
sys.setrecursionlimit(5000000)
n = int(input())
memo = [0 for i in range(n+1)]
def fibo(n):
    if n <= 1:
        memo[n] = n
        return memo[n]
    else:
        if memo[n] > 0:
            return memo[n]
        memo[n] = fibo(n-1)+fibo(n-2)
        return memo[n]
print(fibo(n))
