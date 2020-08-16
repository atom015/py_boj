from sys import *
ip = stdin.readline
N = int(ip())
arr = []
ans,ans1 = {},{}
for i in range(N):
    a,b = map(int,ip().split())
    arr.append([a+500000,b+500000])
arr.append(arr[0])
for i in range(N):
    x1,y1 = arr[i]
    x2,y2 = arr[i+1]
    if x1 == x2:
        for i in range(min(y1,y2),max(y1,y2)):
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
    elif y1 == y2:
        for i in range(min(x1,x2),max(x1,x2)):
            if i in ans1:
                ans1[i] += 1
            else:
                ans1[i] = 1
print(max(list(ans.values())+list(ans1.values())))
