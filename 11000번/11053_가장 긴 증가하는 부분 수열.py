n = int(input())
arr = list(map(int,input().split()))
dp = [0 for i in range(n)]
ans = 0
for i in range(n):
	MAX = 0
	for j in range(i):
		if arr[i] > arr[j]:
			MAX = max(MAX,dp[j])
	dp[i] = MAX+1
print(max(dp))
