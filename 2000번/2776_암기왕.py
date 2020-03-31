from sys import *
ip = stdin.readline
def binary_search(tar):
    s,e = 0,n-1
    while s <= e:
        mid = (s+e)//2
        if arr[mid] < tar:
            s = mid+1
        elif arr[mid] > tar:
            e = mid-1
        else:
            return 1
    return 0
for i in range(int(ip())):
    n = int(ip())
    arr = sorted(list(map(int,ip().split())))
    m = int(ip())
    for i in list(map(int,ip().split())):
        print(binary_search(i))
