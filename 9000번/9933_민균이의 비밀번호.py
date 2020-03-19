arr = []
for i in range(int(input())):
    arr.append(input())
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if arr[i] == arr[j][::-1]:
            print(len(arr[i]),arr[i][len(arr[i])//2])
            break
