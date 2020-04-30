from sys import *
from collections import Counter
ip = stdin.readline
n = int(ip())
arr = list(map(int,ip().split()))
cnt = dict(Counter(arr))
m = int(ip())
for i in list(map(int,input().split())):
    if i in cnt.keys():
        print(cnt[i],end=' ')
    else:
        print(0,end=' ')
