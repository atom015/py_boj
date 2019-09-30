import sys
ip = sys.stdin.readline
n,m = map(int,ip().split())
a = [int(ip()) for i in range(n)]
min_tree = [0]*(4*n)
max_tree = [0]*(4*n)
def init(s,e,nd,tree,c):
    if s == e:
        tree[nd] = a[s]
        return tree[nd]
    m = (s+e)//2
    tree[nd] = c(init(s,m,nd*2,tree,c),init(m+1,e,nd*2+1,tree,c))
    return tree[nd]
init(0,n-1,1,min_tree,min)
init(0,n-1,1,max_tree,max)
def func(s,e,nd,l,r,intger,tree,c):
    if l > e or r < s:
        return intger
    if l <= s and e <= r:return tree[nd]
    m = (s+e)//2
    tmp = c(func(s,m,nd*2,l,r,intger,tree,c),func(m+1,e,nd*2+1,l,r,intger,tree,c))
    return tmp
for i in range(m):
    b,c = map(int,ip().split())
    print(func(0,n-1,1,b-1,c-1,1e9,min_tree,min),func(0,n-1,1,b-1,c-1,0,max_tree,max))
