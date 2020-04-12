from itertools import *
n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
for i in sorted(product(arr,repeat=m)):
    print(*i)
