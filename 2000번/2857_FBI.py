ans = []
for i in range(5):
    s = input()
    if "FBI" in s:
        ans.append(i+1)
if len(ans) == 0:
    print("HE GOT AWAY!")
else:
    print(*ans)