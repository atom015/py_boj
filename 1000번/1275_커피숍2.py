import sys
ip = sys.stdin.readline
n,m = map(int,ip().split())
arr = list(map(int,ip().split()))
tree = [0]*(4*n)
def init(s,e,nd):
    if s == e:
        tree[nd] = arr[s]
        return tree[nd]
    m = (s+e)//2
    tree[nd] = init(s,m,nd*2)+init(m+1,e,nd*2+1)
    return tree[nd]

def Sum(s,e,nd,l,r):
    if l > e or r < s:return 0
    if l <= s and e <= r:return tree[nd]
    m = (s+e)//2
    return Sum(s,m,nd*2,l,r)+Sum(m+1,e,nd*2+1,l,r)
def update(n,s,e,t,dif):
    if s <= t and t <= e:
        tree[n] += dif
    else:
        return
    if s != e:
        m = (s+e)//2
        update(n*2,s,m,t,dif)
        update(n*2+1,m+1,e,t,dif)

init(0,n-1,1)
for i in range(m):
    a,b,c,d = map(int,ip().split())
    if a > b:
        print(Sum(0,n-1,1,b-1,a-1))
    else:
        print(Sum(0,n-1,1,a-1,b-1))
    dif = d-arr[c-1]
    arr[c-1] = d
    update(1,0,n-1,c-1,dif)
