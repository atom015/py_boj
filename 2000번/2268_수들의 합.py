from sys import *
ip = stdin.readline
n,m = map(int,ip().split())
arr = [0]*(n+1)
tree = [0]*(n+1)

def Sum(i):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= (i&-i)
    return ans

def update(i,dif):
    while i <= n:
        tree[i] += dif
        i += (i & -i)

for i in range(m):
    a,b,c = map(int,ip().split())
    if a == 1:
        update(b,c-arr[b])
        arr[b] = c
    else:
        if b > c:
            print(Sum(b)-Sum(c-1))
        else:
            print(Sum(c)-Sum(b-1))
