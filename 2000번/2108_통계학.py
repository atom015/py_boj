import sys
from collections import Counter
t = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for i in range(t)]
def s(t):
    li.sort()
    return li[t//2]
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

print(round(sum(li)/t))
print(s(t))
print(modFinder(li))
print((max(li)+t) - (min(li)+t))
