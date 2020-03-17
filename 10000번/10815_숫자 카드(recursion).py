import sys
sys.setrecursionlimit(5000000)
ip = sys.stdin.readline
n = int(ip())
nli = sorted(list(map(int,ip().split())))
m = int(ip())
def binary(tar,low,high):
    if low > high:
        return False
    mid = (low+high)//2
    if nli[mid] == tar:
        return True
    elif nli[mid] > tar:
        high = mid - 1
    else:
        low = mid + 1
    return binary(tar,low,high)
for i in list(map(int,input().split())):
    if binary(i,0,n-1):
        print(1,end=' ')
    else:
        print(0,end=' ')
