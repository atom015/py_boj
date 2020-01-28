n = int(input())
p = [i for i in range(n+1)]
def gp(x):
    if p[x] == x:return x
    p[x] = gp(p[x])
    return p[x]
def up(a,b):
    a = gp(a)
    b = gp(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b
def find_p(a,b):
    a = gp(a)
    b = gp(b)
    if a == b:return 1
    return 0
for i in range(int(input())):
    a,b = map(int,input().split())
    up(a,b)
cnt = 0
for i in range(2,n+1):
    if find_p(i,1):
        cnt += 1
print(cnt)
