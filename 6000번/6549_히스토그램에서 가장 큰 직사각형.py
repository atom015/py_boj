from sys import *
setrecursionlimit(999999999)
ip = stdin.readline
def init(l,r,nd):
    if l == r:
        tree[nd] = l
    else:
        mid = (l+r)//2
        init(l,mid,nd*2)
        init(mid+1,r,nd*2+1)
        if arr[tree[nd*2]] <= arr[tree[nd*2+1]]:
            tree[nd] = tree[nd*2]
        else:
            tree[nd] = tree[nd*2+1]
def Min(nd,s,e,l,r):
    if l > e or s > r:
        return None
    if l <= s and e <= r:
        return tree[nd]
    mid = (s+e)//2
    t1 = Min(nd*2,s,mid,l,r)
    t2 = Min(nd*2+1,mid+1,e,l,r)
    if t1 == None:return t2
    if t2 == None:return t1
    return t1 if arr[t1] <= arr[t2] else t2

def main(l,r):
    ix = Min(1,0,n-1,l,r)
    ans = (r-l+1)*arr[ix]
    if l <= ix-1:
        ans = max(ans,main(l,ix-1))
    if ix+1 <= r:
        ans = max(ans,main(ix+1,r))
    return ans
while True:
    arr = list(map(int,ip().split()))
    n = arr.pop(0)
    if n == 0:break
    tree = [0]*(n*4)
    init(0,n-1,1)
    print(main(0,n-1))
