from collections import deque
a,b = map(int,input().split())
def bfs(a,b):
    q = deque([[a,1]])
    while q:
        p,cnt = q.popleft()
        if p == b:
            return cnt
        if (p*10)+1 <= b:
            q.append([(p*10)+1,cnt+1])
        if p*2 <= b:
            q.append([p*2,cnt+1])
    return -1
print(bfs(a,b))
