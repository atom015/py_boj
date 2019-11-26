import sys
ip = sys.stdin.readline
n,m,k = map(int,ip().split())
arr = [int(ip()) for i in range(n)]
tree = [0]*(4*n)
def init(s,e,nd):
    if s == e:
        tree[nd] = arr[s]
        return tree[nd]
    m = (s+e)//2
    tree[nd] = (init(s,m,nd*2)*init(m+1,e,nd*2+1))%1000000007
    return tree[nd]
init(0,n-1,1)
def Update(s,e,nd,val,idx):
    if not(s <= idx and idx <= e):
        return tree[nd]
    if s == e:
        tree[nd] = val
        return tree[nd]        
    m = (s+e)//2
    tree[nd] = (Update(s,m,nd*2,val,idx)*Update(m+1,e,nd*2+1,val,idx))%1000000007
    return tree[nd]

def mul(l,r,s,e,nd):
    if l > e or s > r:
        return 1
    if l <= s and e <= r:
        return tree[nd]
    m = (s+e)//2
    return (mul(l,r,s,m,nd*2)*mul(l,r,m+1,e,nd*2+1))%1000000007

for i in range(m+k):
    a,b,c = map(int,ip().split())
    if a == 1:
        Update(0,n-1,1,c,b-1)
    else:
        print(mul(b-1,c-1,0,n-1,1))
