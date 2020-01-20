sum1 = 0
compare = []
for i in range(4):
    n,m = map(int,input().split())
    if n == 0:
        sum1 += m
    else:
        sum1 -= n
        sum1 += m
    compare.append(sum1)
print(max(compare))
