classed = [0,0,0,0,0]
n,k = map(int,input().split())
for i in range(n):
    a,b = map(int,input().split())
    if b == 1 or b == 2:
        classed[0] += 1
    else:
        if a == 1:
            if b == 3 or b == 4:
                classed[1] += 1
            elif b == 5 or b == 6:
                classed[2] += 1
        elif a == 0:
            if b == 3 or b == 4:
                classed[3] += 1
            elif b == 5 or b == 6:
                classed[4] += 1
ans = 0
for i in range(5):
    ans += classed[i]//k
    classed[i] = classed[i]%k
    if classed[i] >= 1:
        ans += 1
print(ans)
