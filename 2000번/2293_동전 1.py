n,k = map(int,input().split())
arr = [int(input()) for i in range(n)]
li = [0 for i in range(k+1)]
li[0] = 1
for i in range(n):
    for j in range(arr[i],k+1):
        li[j] += li[j-arr[i]]
print(li[k])
