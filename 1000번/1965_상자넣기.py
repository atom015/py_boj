n = int(input())
arr = list(map(int,input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    m = 0
    for j in range(i):
        if arr[j] < arr[i]:
            m = max(dp[j],m)
    dp[i] = m+1
print(max(dp))
