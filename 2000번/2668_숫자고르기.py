N = int(input())
arr = [[int(input())-1] for i in range(N)]
v = [False for i in range(N)]
ret = set()
def dfs(nd):
    v[nd] = True
    for i in arr[nd]:
        if not v[i]:
            dfs(i)
        elif cnt[i] < 2:
            cnt[i] += 1
            dfs(i)
        elif cnt[i] == 2:
            cnt[i] += 1
            ans.append(i)
            dfs(i)
for i in range(N):
    cnt = [0 for i in range(N)]
    ans = []
    dfs(i)
    for i in ans:
        ret.add(i)
print(len(ret))
for i in sorted(list(ret)):
    print(i+1)
