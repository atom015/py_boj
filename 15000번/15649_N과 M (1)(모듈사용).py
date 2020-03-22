import itertools
n,m = map(int,input().split())
a = [i for i in range(1,n+1)]
l = list(itertools.permutations(a,m))
for i in sorted(l):
    for j in i:
        print(j,end=' ')
    print()
