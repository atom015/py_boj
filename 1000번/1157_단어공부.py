s = input().upper()
dic = {i:0 for i in s}
for i in s:
    dic[i] += 1
MAX = max(dic.values())
ans = ""
for k,v in dic.items():
    if v == MAX and k not in ans:
        ans += k
print("?" if len(ans) >= 2 else ans)
