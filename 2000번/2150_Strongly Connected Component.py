from sys import *
setrecursionlimit(500000)
ip = stdin.readline
V,E = map(int,ip().split())
arr = [[] for i in range(V+1)]
d = [0 for i in range(V+1)]
f = [False for i in range(V+1)]
scc = []
st = []
SccTotal,cnt = 0,0
for i in range(E):
    a,b = map(int,ip().split())
    arr[a].append(b)
def dfs(nd):
    global cnt,SccTotal
    cnt += 1
    d[nd] = cnt
    st.append(nd)

    p = d[nd]
    for i in arr[nd]:
        if d[i] == 0:
            p = min(p,dfs(i))
        elif not f[i]:
            p = min(p,d[i])
    if p == d[nd]:
        sc = []
        while 1:
            t = st.pop()
            sc.append(t)
            f[t] = True
            if t == nd:break
        sc.sort()
        scc.append(sc)
        SccTotal += 1

    return p
for i in range(1,V+1):
    if d[i] == 0:
        dfs(i)
scc.sort()
print(SccTotal)
for i in scc:
    print(*i,end=' ')
    print(-1)
