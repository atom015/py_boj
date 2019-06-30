n = int(input())
m = int(input())
cnt = 0
chk = [False for i in range(n+1)]
li = [[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    li[a].append(b)
    li[b].append(a)
def dfs(nd):
    for i in range(len(li[nd])):
        tmp = li[nd][i]
        chk[tmp] = True
    if nd == 1:
        for i in range(len(li[nd])):
            tmp = li[nd][i]
            dfs(tmp)
dfs(1)
print(chk.count(True)-1)
