t = int(input())
arr = [[] for i in range(t+1)]
v = [False for i in range(t+1)]
s,e = map(int,input().split())
for i in range(int(input())):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(s,e):
    q = [[s,0]]
    v[s] = True
    while q:
        p,cnt = q.pop(0)
        if p == e:
            return cnt
        for i in arr[p]:
            if v[i] != True:
                v[i] = True
                q.append([i,cnt+1])
    return -1
print(bfs(s,e))
