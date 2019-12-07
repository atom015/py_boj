from collections import deque
import sys
ip = sys.stdin.readline
n,m = map(int,ip().split())
arr = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,ip().split())
    arr[b-1].append(a-1)
ret = []
for i in range(n):
    q = deque([i])
    v = [False for i in range(n+1)]
    v[i] = True
    cnt = 0
    while q:
        nd = q.popleft()
        for i in arr[nd]:
            if v[i] == False:
                cnt += 1
                q.append(i)
                v[i] = True
    ret.append(cnt)
M = max(ret)
for i in range(n):
    if ret[i] == M:
        print(i+1,end=' ')
