n = int(input())
inf = 1e9
arr = [[0 for i in range(n)] for i in range(n)]
m = int(input())
for i in range(n):
	arr[i][i] = 1
for i in range(m):
	a,b = map(int,input().split())
	arr[a-1][b-1] = 1
for i in range(n):
	for j in range(n):
		for k in range(n):
			if arr[j][i] and arr[i][k]:
				arr[j][k] = 1

for i in range(n):
	cnt = 0
	for j in range(n):
		if arr[i][j] == 0 and arr[j][i] == 0:
			cnt += 1
	print(cnt)
		
