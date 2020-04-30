ans = 0
mo = ["a","e","i","o","u"]
n = list(input())
for i in n:
    if i in mo:
        ans += 1
print(ans)
