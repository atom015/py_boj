import sys
ip = sys.stdin.readline
n = int(ip())
arr = sorted(list(map(int,ip().split())))
m = int(ip())
def binary(tar):
    s,e = 0,n
    while s < e:
        mid = (s+e)//2
        if arr[mid] == tar:
            return True
        if arr[mid] < tar:
            s = mid+1
        if arr[mid] > tar:
            e = mid
    return False
for i in list(map(int,ip().split())):
    if binary(i):
        print(1,end=' ')
    else:
        print(0,end=' ')
