n = int(input())
dp = [0 for i in range(n)]
arr = list(map(int,input().split()))
for i in range(n):
    c = 0
    for j in range(i):
        if arr[i] < arr[j]:
            c = max(c,dp[j])
    dp[i] = c+1
print(max(dp))
