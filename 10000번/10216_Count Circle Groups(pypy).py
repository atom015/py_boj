from math import sqrt
def dfs(nd):
    v[nd] = True
    for i in arr[nd]:
        if v[i] == False:
            dfs(i)
def node_connect():
    for i in range(1,n+1):
        for j in range(1,i+1):
            x1,y1,w1 = li[i]
            x2,y2,w2 = li[j]
            x = x1-x2
            y = y1-y2
            r = w1+w2
            d = sqrt(x*x + y*y)
            if d <= r:
                arr[i].append(j)
                arr[j].append(i)

for i in range(int(input())):
    n = int(input())
    ans = 0
    arr = [[i] for i in range(n+1)]
    v = [False for i in range(n+1)]
    li = [0]
    for i in range(n):
        li.append(list(map(int,input().split())))
    node_connect()
    for i in range(1,n+1):
        if v[i] == False:
            dfs(i)
            ans += 1
    print(ans)
