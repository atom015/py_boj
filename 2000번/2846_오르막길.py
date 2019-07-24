n = int(input())
li = list(map(int,input().split()))
compare = 0
sd = set()
result = []
chk = False
def minus(l):
    m = 0
    for i in range(len(l)):
        if i != len(l)-1:
            m += l[i]-l[i+1]
    return m
for i in range(n):
    if i >= 1:
        compare = li[i-1]
        if compare < li[i]:
            chk = True
            sd.add(compare)
            sd.add(li[i])
        else:
            l = list(sd)
            l.sort(reverse=True)
            result.append(minus(l))
            sd = set()
if chk == False and len(result) == 0 and len(sd) >= 1:
    print(0)
    exit()
l = list(sd)
l.sort(reverse=True)
result.append(minus(l))
print(max(result))
