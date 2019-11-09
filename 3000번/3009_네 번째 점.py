arr = [[],[]]
for i in range(3):
    a,b = map(int,input().split())
    if a not in arr[0]:
        arr[0].append(a)
    else:
        arr[0].remove(a)
    if b not in arr[1]:
        arr[1].append(b)
    else:
        arr[1].remove(b)
print(arr[0][0],arr[1][0])