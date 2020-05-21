from sys import *
from collections import deque
ip = stdin.readline
N,d,k,c = map(int,ip().split())
arr = [int(ip()) for i in range(N)]
dq,chk,ans,cnt = deque([]),[0]*(d+1),0,0

for i in range(k):
    dq.append(arr[i])
    if not chk[arr[i]]:
        cnt += 1
    chk[arr[i]] += 1

ans = max(ans,cnt)

for i in range(k,k+N):
    dq.popleft()

    chk[arr[i-k]] -= 1
    if not chk[arr[i-k]]:
        cnt -= 1

    dq.append(arr[i%N])
    if not chk[arr[i%N]]:
        cnt += 1
    chk[arr[i%N]] += 1

    if not chk[c]:
        ans = max(ans,cnt+1)
    else:
        ans = max(ans,cnt)
print(ans)
