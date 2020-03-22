from itertools import *
n,m = map(int,input().split())
arr = list(map(int,input().split()))
li = permutations(arr,m)
for i in sorted(li):
    print(*i)
