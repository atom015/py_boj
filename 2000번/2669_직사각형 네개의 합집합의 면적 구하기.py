arr = [[0 for i in range(102)] for i in range(102)]
for i in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] = 1
cnt = 0
for i in arr:
    cnt += i.count(1)
print(cnt)
