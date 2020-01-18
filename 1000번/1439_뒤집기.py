s = input()
ans = [0,0]
if s[0] == "0":
    ans[0] = 1
else:
    ans[1] = 1
for i in range(1,len(s)):
    if s[i] != s[i-1]:
        if s[i] == "0":
            ans[0] += 1
        else:
            ans[1] += 1
print(min(ans))
