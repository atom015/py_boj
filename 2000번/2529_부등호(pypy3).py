from operator import *
from itertools import permutations
from sys import *
ip = stdin.readline
k = int(ip())
inq = []
for i in list(ip().split()):
    if i == "<":
        inq.append(lt)
    else:
        inq.append(gt)
ans = []
arr = [str(i) for i in range(10)]
for i in permutations(arr,k+1):
    chk = True
    for j in range(k):
        if not inq[j](i[j],i[j+1]):
            chk = False
    if chk:
        ans.append(i)
print("".join(ans[-1]))
print("".join(ans[0]))
