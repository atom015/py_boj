n,m = map(int,input().split())
arr = [[] for i in range(n+1)]
ind = [0 for i in range(n+1)]
ans = []
for i in range(m):
    tmp = list(map(int,input().split()))
    k = tmp.pop(0)
    for i in range(k-1):
        arr[tmp[i]].append(tmp[i+1])
        ind[tmp[i+1]] += 1
def topg():
    q = []
    for i in range(1,n+1):
        if ind[i] == 0:
            q.append(i)
    while q:
        p = q.pop(0)
        ans.append(p)
        for i in arr[p]:
            ind[i] -= 1
            if ind[i] == 0:
                q.append(i)
topg()
if len(ans) == n:
    for i in ans:
        print(i)
else:
    print(0)
