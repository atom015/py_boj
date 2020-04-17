n,m = map(int,input().split())
cnt = 1
arr = []
for i in range(m):
    for j in range(cnt):
        arr.append(cnt)
    cnt += 1
print(sum(arr[n-1:m]))
