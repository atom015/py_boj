n = int(input())
ans = 0
i = 1
for i in range(1,n+1):
    s = list(str(i))
    s = [int(i) for i in s]
    c = i + sum(s)
    if c == n:
        ans = i
        break
print(ans)
