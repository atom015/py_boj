n = int(input())
inf = 1e9
arr = [[inf for i in range(n)] for i in range(n)]
for i in range(n):
    arr[i][i] = 0
while 1:
    a,b = map(int,input().split())
    if a == b == -1:
        break
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            tmp = arr[i][k]+arr[k][j]
            if tmp < inf:
                arr[i][j] = min(arr[i][j],tmp)
ret = [0 for i in range(n)]
for i in range(n):
    ret[i] = max(arr[i])
mi = min(ret)
ans = []
for i in range(n):
    if ret[i] == mi:
        ans.append(i+1)
print(mi,len(ans))
print(*ans)
