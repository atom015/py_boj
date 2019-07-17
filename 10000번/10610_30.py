n = list(input())
n.sort(reverse=True)
tmp = "".join(n)
if int(tmp) % 30 == 0:
    print(int(tmp))
else:
    print(-1)
