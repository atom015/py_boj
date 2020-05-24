K,N = map(int,input().split())
arr = [int(input()) for i in range(K)]
def checking(mid):
    t = 0
    for i in arr:
        t += i//mid
    if t >= N:
        return 1
def binary():
    s,e,ret = 1,max(arr),0
    while s <= e:
        mid = (s+e)//2
        if checking(mid):
            s = mid+1
            ret = max(ret,mid)
        else:
            e = mid-1
    return ret
print(binary())
