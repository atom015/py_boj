n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:(x[1],x[0]))
cnt = 1
e = arr[0][1]
for i in range(1,n):
    if e <= arr[i][0]:
        e = arr[i][1]
        cnt += 1
print(cnt)
