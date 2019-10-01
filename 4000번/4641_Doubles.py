while 1:
    arr = list(map(int,input().split()))
    cnt = 0
    if arr[0] == -1 and len(arr) == 1:
        break
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if arr[i]*2 == arr[j]:
                    cnt += 1
    print(cnt)
