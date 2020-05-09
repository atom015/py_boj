a,b,c,d  = map(int,input().split())
v = {}
v[(0,0)] = 1
q = [[0,0,0]]
ans = 1e9
def M(x,y):
    if x+y > b:
        return [x+y-b,b]
    return [0,y+x]
def M1(x,y):
    if x+y > a:
        return [a,x+y-a]
    return [x+y,0]
while q:
    x,y,cnt = q.pop(0)
    if [x,y] == [c,d]:
        ans = min(cnt,ans)
    else:
        if not bool(v.get((0,y))):
            q.append([0,y,cnt+1])
            v[(0,y)] = 1
        if not bool(v.get((x,0))):
            q.append([x,0,cnt+1])
            v[(x,0)] = 1
        if not v.get((a,y)):
            q.append([a,y,cnt+1])
            v[(a,y)] = 1
        if not v.get((x,b)):
            q.append([x,b,cnt+1])
            v[(x,b)] = 1
        m,m1 = M(x,y),M1(x,y)
        if not v.get((m[0],m[1])):
            q.append(m+[cnt+1])
            v[(m[0],m[1])] = 1
        if not v.get((m1[0],m1[1])):
            q.append(M1(x,y)+[cnt+1])
            v[(m1[0],m1[1])] = 1
print(-1 if ans == 1e9 else ans)
