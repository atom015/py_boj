n,k = map(int,input().split())
arr = []
for i in range(1,k+1):
    tmp = str(n*i)
    arr.append(int(tmp[::-1]))
print(max(arr))
