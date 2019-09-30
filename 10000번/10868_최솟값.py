import sys
ip = sys.stdin.readline
n,m = map(int,ip().split())
a = [int(ip()) for i in range(n)]
tree = [0]*(4*n)
def init(s,e,nd):
    if s == e:
        tree[nd] = a[s]
        return tree[nd]
    m = (s+e)//2
    tree[nd] = min(init(s,m,nd*2),init(m+1,e,nd*2+1))
    return tree[nd]
init(0,n-1,1)
def Min(s,e,nd,l,r):
    if l > e or r < s:
        return 1e9
    if l <= s and e <= r:return tree[nd]
    m = (s+e)//2
    tmp = min(Min(s,m,nd*2,l,r),Min(m+1,e,nd*2+1,l,r))
    return tmp
for i in range(m):
    b,c = map(int,ip().split())
    print(Min(0,n-1,1,b-1,c-1))
