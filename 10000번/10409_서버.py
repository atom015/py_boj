n,t = map(int,input().split())
a = list(map(int,input().split()))
s = 0
cnt = 0
for i in range(n):
    if s+a[i] > t:
        break
    else:
        s += a[i]
        cnt += 1
print(cnt)
