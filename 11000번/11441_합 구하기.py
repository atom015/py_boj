n = int(input())
arr = [0]+list(map(int,input().split()))
tree = [0]*(n*4)
def init(s,e,nd):
    if s == e:
        tree[nd] = arr[s]
        return tree[nd]
    m = (s+e)//2
    tree[nd] = init(s,m,nd*2)+init(m+1,e,nd*2+1)
    return tree[nd]
init(1,n,1)
def Sum(s,e,nd,l,r):
    if l > e or r < s:return 0
    if l <= s and e <= r:return tree[nd]
    m = (s+e)//2
    return Sum(s,m,nd*2,l,r)+Sum(m+1,e,nd*2+1,l,r)
for i in range(int(input())):
    a,b = map(int,input().split())
    print(Sum(1,n,1,a,b))
