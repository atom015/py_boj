import sys
sys.setrecursionlimit(5000000)
def dfs(nd):
    if v[nd] == True:
        return
    v[nd] = True
    dfs(arr[nd])
for _ in range(int(input())):
    cnt = 0
    n = int(input())
    arr = [0]+list(map(int,input().split()))
    v = [0]+[False for i in range(n)]
    for i in range(1,n+1):
        if v[i] == False:
            dfs(i)
            cnt += 1
    print(cnt)
