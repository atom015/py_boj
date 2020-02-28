import sys
ip = sys.stdin.readline
n,m = map(int,ip().split())
inf = 1e9
arr = [[1e9 for i in range(400)] for i in range(400)]
for i in range(n):
    arr[i][i] = 1
for i in range(m):
	a,b = map(int,ip().split())
	arr[a-1][b-1] = 1
for i in range(n):
    for j in range(n):
        for k in range(n):
            arr[j][k] = min(arr[j][k],arr[j][i]+arr[i][k])

for i in range(int(ip())):
	a,b = map(int,ip().split())
	if arr[a-1][b-1] != inf:
		print(-1)
	elif arr[b-1][a-1] != inf:
		print(1)
	else:
		print(0)
