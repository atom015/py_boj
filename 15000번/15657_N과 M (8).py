from itertools import *
n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
for i in sorted(combinations_with_replacement(arr,m)):
    print(*i)
