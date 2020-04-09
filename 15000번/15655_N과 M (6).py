from itertools import *
n,m = map(int,input().split())
arr = list(map(int,input().split()))
for i in sorted(permutations(arr,m)):
    if list(i) == sorted(list(i)):
        print(*i)
