from itertools import *
from sys import *
ip = stdin.readline
n,m = map(int,ip().split())
arr = sorted(ip().split())
li = combinations(arr,n)
for i in li:
    cnt = [0,0]
    for j in i:
        if j in ["a","e","i","o","u"]:
            cnt[0] += 1
        else:
            cnt[1] += 1
    if cnt[0] >= 1 and cnt[1] >= 2:
        print("".join(i))
