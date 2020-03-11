s = list(input())
bar = 0
cnt = 0
for i in s:
    if i == "(":
        bar += 1
    else:
        bar -= 1
        if p == "(":
            cnt += bar
        else:
            cnt += 1
    p = i
print(cnt)
