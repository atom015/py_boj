n,m = map(int,input().split())
cost = []
Exf = []
ans = [0 for i in range(n)]
for i in range(n):
    cost.append(int(input()))
for i in range(m):
    Exf.append(int(input()))
for i in range(m):
    for j in range(n):
        if Exf[i] >= cost[j]:
            ans[j] += 1
            break
print(ans.index(max(ans))+1)
