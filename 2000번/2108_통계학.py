import sys
from collections import Counter
from statistics import median
n = []
t = int(sys.stdin.readline())

for i in range(t):
    n.append(int(sys.stdin.readline()))

def san(n):
    global t
    return round(sum(n) / t)

def meadian(t):
    t.sort()
    return median(t)

def modFinder(nBox):
    cntDic = Counter(nBox)
    cntTpl = cntDic.most_common()
    if len(nBox) > 1:
        if cntTpl[0][1] == cntTpl[1][1]:
            mod = cntTpl[1][0]
        else:
            mod = cntTpl[0][0]
    else:
        mod = cntTpl[0][0]

    return mod

def range(k):
    global t
    return (max(k)+t) - (min(k)+t)


print(san(n))
print(meadian(n))
print(modFinder(n))
print(range(n))
