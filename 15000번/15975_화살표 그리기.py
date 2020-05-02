from sys import *
ip = stdin.readline
n = int(ip())
arr = []
for i in range(n):
    a,b = map(int,ip().split())
    arr.append([a,b])
arr.sort(key=lambda x:[x[1],x[0]])
s = 0
for i in range(n):
    if n != 1:
        if i == 0:
            if arr[i][1] == arr[i+1][1]:
                s += abs(arr[i][0]-arr[i+1][0])
        elif i == n-1:
            if arr[i-1][1] == arr[i][1]:
                s += abs(arr[i][0]-arr[i-1][0])
        elif arr[i][1] == arr[i+1][1] and arr[i-1][1] == arr[i][1]:
            s += min(abs(arr[i+1][0]-arr[i][0]),abs(arr[i][0]-arr[i-1][0]))
        elif arr[i][1] == arr[i+1][1]:
            s += abs(arr[i+1][0]-arr[i][0])
        elif arr[i-1][1] == arr[i][1]:
            s += abs(arr[i][0]-arr[i-1][0])

print(s)
