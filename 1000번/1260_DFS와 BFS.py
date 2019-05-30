n,m,start = map(int,input().split())
li = [[0 for i in range(n)] for i in range(n)]
chk = [False for i in range(n)]
visited = [False for i in range(n)]
Queue = [start]
def dfs(nd,n):
    print(nd+1,end=' ')
    chk[nd] = True
    for i in range(n):
        if li[nd][i] == 1 and chk[i] == False:
            dfs(i,n)
for i in range(m):
    a,b = map(int,input().split())
    li[a-1][b-1] = 1
    li[b-1][a-1] = 1
dfs(start-1,n)
print()
while len(Queue) != 0:
    p = Queue.pop(0)-1
    print(p+1,end=' ')
    visited[p] = True
    for i in range(n):
        if li[p][i] == 1 and visited[i] == False:
            visited[i] = True
            Queue.append(i+1)
