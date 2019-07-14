compare = 0
n,m = map(int,input().split())
li = list(map(int,input().split()))
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum = li[i]+li[j]+li[k]
            if sum == m:
                print(sum)
                exit()
            elif compare < sum < m:
                compare = sum
print(compare)
