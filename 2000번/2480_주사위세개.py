num = [0,0,0]
cnt = 0
n = list(map(int,input().split()))
for i in range(len(n)):
    for j in range(len(n)):
        if i < j or i > j:
            if n[i] == n[j]:
                if num[0] == 0:
                    num[0] = n[i]
                num[i] = n[i]
    if num[i] > 0:
        cnt += 1
if cnt == 3:
    print(10000 + num[0] * 1000)
elif cnt == 2:
    print(1000 + num[0] * 100)
else:
    print(max(n) * 100)
