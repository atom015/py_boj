n,m = map(int,input().split())
inf = 1e9
arr = [[inf for i in range(n)] for i in range(n)]
for i in range(n):
    arr[i][i] = 0
for i in range(m):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1


def floy():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                arr[i][j] = min(arr[i][j],arr[i][k]+arr[k][j])
floy()
ret = [0 for i in range(n)]
for i in range(n):
    ret[i] = sum(arr[i])
mi = min(ret)
for i in range(n):
    if ret[i] == mi:
        print(i+1)
        break
