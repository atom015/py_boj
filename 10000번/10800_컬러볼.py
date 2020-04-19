from sys import *
ip = stdin.readline
n = int(ip())
ans = [0]*n
arr = []
c = [0]*n
total = 0
for i in range(n):
    a,b = map(int,ip().split())
    arr.append([a-1,b,i])
arr = sorted(arr,key=lambda x:x[1])
j = 0
for co,s,ix in arr:
    while arr[j][1] < s:
        total += arr[j][1]
        c[arr[j][0]] += arr[j][1]
        j += 1
    ans[ix] = total-c[co]
for i in ans:
    print(i)
