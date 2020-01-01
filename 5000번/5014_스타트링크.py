f,s,g,u,d = map(int,input().split())
q = [[s,0]]
v = [False for i in range(f+1)]
v[s] = True
def bfs():
    while q:
        now,cnt = q.pop(0)
        if now == g:
            return cnt
        if 0 <= now-d and not(v[now-d]):
            q.append([now-d,cnt+1])
            v[now-d] = True
        if now+u <= f and not(v[now+u]):
            q.append([now+u,cnt+1])
            v[now+u] = True
    return "use the stairs"
print(bfs())
