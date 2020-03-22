import sys
ip = sys.stdin.readline
n,m = map(int,ip().split())
arr = [0]+[int(ip()) for i in range(n)]
tree = [0]*(4*n)
def init(s,e,nd):
    if s == e:
        tree[nd] = arr[s]
        return tree[nd]
    mid = (s+e)//2
    tree[nd] = min(init(s,mid,nd*2),init(mid+1,e,nd*2+1))
    return tree[nd]
init(1,n,1)
def Min(s,e,nd,l,r):
    if e < l or s > r:
        return 1e9*100
    if l <= s and e <= r:return tree[nd]
    mid = (s+e)//2
    return min(Min(s,mid,nd*2,l,r),Min(mid+1,e,nd*2+1,l,r))
for i in range(m):
    a,b = map(int,ip().split())
    print(Min(1,n,1,a,b))
