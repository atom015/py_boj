import sys
ip = sys.stdin.readline
def gp(x):
    if p[x] == x:
        return p[x]
    p[x] = gp(p[x])
    return p[x]
def up(a,b):
    a = gp(a)
    b = gp(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b
def ch(a,b):
    a = gp(a)
    b = gp(b)
    if a == b:
        return True
    return False
arr = []
ans = 0
n,m = map(int,input().split())
p = [i for i in range(n+1)]
for i in range(m):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:(x[2]))
for i in range(m):
    a,b,c = arr[i]
    if ch(a,b) == False:
        up(a,b)
        ans += c
print(ans)
