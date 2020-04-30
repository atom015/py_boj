cnt = 0
coin = []
n,k = map(int,input().split())
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
for i in range(n):
    if coin[i] <= k:
        cnt += k // coin[i]
        k = k % coin[i]
print(cnt)
