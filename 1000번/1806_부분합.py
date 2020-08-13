N,S = map(int,input().split())
arr = list(map(int,input().split()))
e,Sum,ans = 0,0,1e9
for s in range(N):
    while e < N and Sum < S:
        Sum += arr[e]
        e += 1
    if S <= Sum:
        ans = min(max(s,e)-min(s,e),ans)
    Sum -= arr[s]
print(0 if ans == 1e9 else ans)
