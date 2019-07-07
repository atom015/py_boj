n = input().upper()
chk = {i:0 for i in set(n)}
for i in n:
    chk[i] += 1
max = max(chk.values())
result = set(k for k,v in chk.items() if max == v)
if len(result) == 1:
    print(result.pop())
else:
    print("?")
