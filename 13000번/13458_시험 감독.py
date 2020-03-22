n = int(input())
arr = list(map(int,input().split()))
b,c = map(int,input().split())
cnt = 0
for i in range(n):
    cnt += 1
    arr[i] -= b
    if arr[i] > 0:
        div,mod = divmod(arr[i],c)
        cnt += div
        if mod > 0:
            cnt += 1
print(cnt)
