com = int(input())
net = int(input())
li = [[0 for i in range(com)] for i in range(com)]
visted = [False for i in range(com)]
for i in range(net):
    a,b = map(int,input().split())
    li[a-1][b-1] = 1
    li[b-1][a-1] = 1
cnt = 0
def dfs(nd,n):
    global cnt
    nd = nd-1
    visted[nd] = True
    for i in range(n):
        if li[nd][i] == 1 and visted[i] == False:
            cnt += 1
            dfs(i+1,n)
dfs(1,com)
print(cnt)
