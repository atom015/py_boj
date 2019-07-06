li = [input() for i in range(int(input()))]
overlap = set(i[0] for i in li)
chk = {i:0 for i in overlap}
for i in li:
    chk[i[0]] += 1
result = []
for k,v in chk.items():
    if v >= 5:
        result.append(k)
if len(result) == 0:
    print("PREDAJA")
else:
    for i in sorted(result):
        print(i,end='')
