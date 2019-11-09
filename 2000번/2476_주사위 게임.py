n = int(input())
money = []
for i in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        money.append(10000 + a * 1000)
    elif a == c or a == b:
        money.append(1000 + a * 100)
    elif b == c:
        money.append(1000 + b * 100)
    else:
        money.append(max(a, b, c) * 100)

print(max(money))


