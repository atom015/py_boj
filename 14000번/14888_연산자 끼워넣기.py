n = int(input())
arr = list(map(int,input().split()))
a,b,c,d = map(int,input().split())
MIN,MAX = 1e9,-1e9
def dfs(ix,pl,mi,mu,di,s):
    global MAX,MIN
    if ix == n-1:
        MAX = max(MAX,s)
        MIN = min(MIN,s)
    else:
        if pl < a:
            dfs(ix+1,pl+1,mi,mu,di,s+arr[ix+1])
        if mi < b:
            dfs(ix+1,pl,mi+1,mu,di,s-arr[ix+1])
        if mu < c:
            dfs(ix+1,pl,mi,mu+1,di,s*arr[ix+1])
        if di < d:
            dfs(ix+1,pl,mi,mu,di+1,int(s/arr[ix+1]))
dfs(0,0,0,0,0,arr[0])
print(MAX)
print(MIN)
