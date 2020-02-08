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
for i in range(int(ip())):
    n,m = map(int,ip().split())
    p = [i for i in range(n+1)]
    arr = []
    ans = 0
    for i in range(m):
        a,b = map(int,ip().split())
        arr.append([a,b])
    for i in range(m):
        if ch(arr[i][0],arr[i][1]) == False:
            up(arr[i][0],arr[i][1])
            ans += 1
    print(ans)
