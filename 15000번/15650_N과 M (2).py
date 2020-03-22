from itertools import *
n,m = map(int,input().split())
arr = [i+1 for i in range(n)]
li = permutations(arr,m)
for i in li:
    i = list(i)
    if i == sorted(i):
        for j in i:
            print(j,end=' ')
        print()
