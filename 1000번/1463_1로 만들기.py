def bfs(n):
    q = [[n,0]]
    chk = [n]
    while len(q) != 0:
        p,cnt = q.pop(0)
        if p == 1:
            return cnt
            break
        if p % 3 == 0 and p//3 not in chk:
            q.append([p//3,cnt+1])
            chk.append(p//3)
        if p % 2 == 0 and p//2 not in chk:
            q.append([p//2,cnt+1])
            chk.append(p//2)
        if p-1 not in chk:
            q.append([p-1,cnt+1])
            chk.append(p-1)
    return cnt
n = int(input())
print(bfs(n))
