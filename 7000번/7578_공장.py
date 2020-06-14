N = int(input())
A = list(map(int,input().split()))
t = list(map(int,input().split()))
B = {t[i]:i+1 for i in range(N)}
tree,ret = [0]*(N+1),0
def Sum(i):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= (i & -i)
    return ans

def update(i,dif):
    while i <= N:
        tree[i] += dif
        i += (i & -i)

for i in range(N):
    ix = B[A[i]]
    ret += Sum(N)-Sum(ix)
    update(ix,1)
print(ret)
