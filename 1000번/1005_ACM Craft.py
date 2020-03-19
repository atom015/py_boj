import sys
ip = sys.stdin.readline
for _ in range(int(ip())):
    n,k = map(int,ip().split())
    dist = [0]+list(map(int,ip().split()))
    ans = [0 for i in range(n+1)]
    arr = [[] for i in range(n+1)]
    inD = [0 for i in range(n+1)]
    for i in range(k):
        a,b = map(int,ip().split())
        arr[a].append(b)
        inD[b] += 1
    last = int(ip())
    q = []
    for i in range(1,n+1):
        if inD[i] == 0:
            q.append(i)
    while inD[last] > 0:
        p = q.pop(0)
        for i in arr[p]:
            inD[i] -= 1
            ans[i] = max(ans[i],ans[p]+dist[p])
            if inD[i] == 0:
                q.append(i)
    print(ans[last]+dist[last])
