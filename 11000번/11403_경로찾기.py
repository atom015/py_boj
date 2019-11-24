n = int(input())
arr = [list(map(int,input().split())) for i in range(n)]
def floy():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if arr[i][k]+arr[k][j] >= 2:
                    arr[i][j] = 1
floy()
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()
