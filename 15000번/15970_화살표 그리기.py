s = 0
n = int(input())
arr = [[] for i in range(n)]
for i in range(n):
    a,b = map(int,input().split())
    arr[b-1].append(a)
    arr[b-1].sort()
for i in range(n):
    for j in range(len(arr[i])):
        if j == len(arr[i])-1:
            s += abs(arr[i][j-1]-arr[i][j])
        elif j == 0:
            s += abs(arr[i][j+1]-arr[i][j])
        else:
            s += min(abs(arr[i][j+1]-arr[i][j]),abs(arr[i][j-1]-arr[i][j]))

print(s)
