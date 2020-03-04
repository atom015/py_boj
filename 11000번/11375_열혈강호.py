import sys
sys.setrecursionlimit(999999999)
n,m = map(int,input().split())
arr = [[] for i in range(1000+1)]
d = [0 for i in range(1000+1)]
c = [False for i in range(1000+1)]

def dfs(nd):
    for i in arr[nd]:
        if c[i]:continue
        c[i] = True
        if d[i] == 0 or dfs(d[i]):
            d[i] = nd
            return True
    return False
for i in range(1,n+1):
    li = list(map(int,input().split()))
    k = li[0]
    for j in range(1,len(li)):
        arr[i].append(li[j])
cnt = 0
for i in range(1,n+1):
    c = [False for i in range(1000+1)]
    if dfs(i):cnt += 1
print(cnt)
