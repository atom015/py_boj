from collections import deque
N,L = map(int,input().split())
arr = list(map(int,input().split()))
dq = deque([])
for i in range(N):
    if dq and dq[0][1] <= i-L:
        dq.popleft()
    while dq and dq[-1][0] >= arr[i]:
        dq.pop()
    dq.append((arr[i],i))
    print(dq[0][0],end=' ')
