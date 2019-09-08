arr = [0 for i in range(9)]
visited = [False for i in range(9)]
n,m = map(int,input().split())
def func(cnt):
    if cnt == m:
        for i in range(m):
            print(arr[i],end=' ')
        print()
    for i in range(1,n+1):
        if visited[i] == False:
            visited[i] = True
            arr[cnt] = i
            func(cnt+1)
            visited[i] = False
func(0)
