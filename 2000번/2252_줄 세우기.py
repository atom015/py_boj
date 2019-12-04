n,m = map(int,input().split())
inDegree = [0 for i in range(n+1)]
arr = [[] for i in range(n+1)]
ret = [0 for i in range(n+1)]
def topologySort():
    q = []
    for i in range(1,n+1):
        if inDegree[i] == 0:
            q.append(i)
    for i in range(1,n+1):
        p = q.pop(0)
        ret[i] = p
        for j in range(len(arr[p])):
            y = arr[p][j]
            inDegree[y] -= 1
            if inDegree[y] == 0:
                q.append(y)
    for i in range(1,n+1):
        print(ret[i],end=' ')
for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    inDegree[b] += 1

topologySort()
