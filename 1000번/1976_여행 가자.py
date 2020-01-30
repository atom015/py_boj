def gp(p,x):
    if p[x] == x:
        return x
    p[x] = gp(p,p[x])
    return p[x]
def up(p,a,b):
    a = gp(p,a)
    b = gp(p,b)
    if a < b:
        p[b] = a
    else:
        p[a] = b
def fp(p,a,b):
    a = gp(p,a)
    b = gp(p,b)
    if a == b:
        return 1
    return 0
n = int(input())
m = int(input())
p = [i for i in range(m+1)]
arr = [list(map(int,input().split())) for i in range(n)]
plan = list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            up(p,i+1,j+1)
c = p[plan[0]]
for i in range(1,len(plan)):
    if c != p[plan[i]]:
        print("NO")
        exit()
print("YES")
