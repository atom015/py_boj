n = input()
arr = []
for i in range(len(n)):
    arr += n[i]
    arr = [int(i) for i in arr]
    arr.sort()
    arr.reverse()

for i in range(len(arr)):
    print(arr[i],end='')
