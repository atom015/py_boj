N,M = map(int,input().split())
arr = sorted(list(map(int,input().split())))
def point(val):
    s = 0
    for i in arr:
        s += i-val if i > val else 0
    return s
def lower_bound():
    s,e,ans = 0,max(arr),0
    while s <= e:
        mid = (s+e)//2
        p = point(mid)
        if p >= M:
            ans = max(ans,mid)
            s = mid+1
        else:
            e = mid-1
    return ans
print(lower_bound())
