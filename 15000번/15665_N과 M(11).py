from itertools import *
n,m = map(int,input().split())
arr = list(map(int,input().split()))
for i in sorted(list(set(product(arr,repeat=m)))):
    print(*i)
