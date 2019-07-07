n = int(input())
nl = sorted(list(map(int,input().split())))
m = int(input())
ml = list(map(int,input().split()))
#이진검색으로 해주면된다.
def binary_search(n,lo,hi,li):
    if lo > hi:
        return 0
    mid = (lo+hi) // 2
    if li[mid] == n:
        return 1
    if li[mid] < n:
        lo = mid + 1
    else:
        hi = mid - 1
    return binary_search(n,lo,hi,li)
for i in ml:
    print(binary_search(i,0,n-1,nl))
