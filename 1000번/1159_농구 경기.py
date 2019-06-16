n = int(input())
li = [input() for i in range(n)]
result = []
chk = {}
for i in li:
    if i[0] not in chk:
        chk[i[0]] = 1
for i in range(n):
    for j in range(n):
        if i != j:
            if li[j] != None and li[i] != None and li[i][0] == li[j][0]:
                chk[li[i][0]] += 1
                li[j] = None
for k,v in chk.items():
    if v >= 5:
        result.append(k)
if len(result) == 0:
    print("PREDAJA")
else:
    for i in sorted(result):print(i,end='')
