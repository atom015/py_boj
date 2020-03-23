N = int(input())
arr = sorted(list(map(int,input().split())))
M = int(input())
def point(val):
    s = 0
    for i in arr:
        s += val if i > val else i
    return s
def lower_bound():
    s,e,ans = 0,max(arr),0
    while s <= e:
        mid = (s+e)//2
        p = point(mid)
        if p <= M:
            ans = max(ans,mid)
            s = mid+1
        else:
            e = mid-1
    return ans
print(lower_bound())
