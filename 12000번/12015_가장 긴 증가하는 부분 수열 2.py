from sys import *
ip = stdin.readline
N = int(ip())
arr = list(map(int, ip().split()))
dp = [0]*(N+5)
dp[0] = arr[0]
ix = 0


def binary(n, t):
	s, e = 0, n
	while s < e:
		mid = (s+e)//2
		if dp[mid] >= t:
			e = mid
		else:
			s = mid+1

	return e


for i in range(1, N):
	if dp[ix] < arr[i]:
		dp[ix+1] = arr[i]
		ix += 1
	else:
		j = binary(ix, arr[i])
		dp[j] = arr[i]
print(ix+1)
