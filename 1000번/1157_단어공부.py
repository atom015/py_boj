n = input().upper() #대소문자는 구분하지않으니까 대문자로 바꾸어주었다.
chk = {i:0 for i in set(n)}
for i in n:
    chk[i] += 1
max = max(chk.values())
result = set(k for k,v in chk.items() if max == v)
if len(result) == 1:
    print(result.pop())
else:
    print("?")
