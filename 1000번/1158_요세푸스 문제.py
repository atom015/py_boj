from collections import deque
n,k = map(int,input().split())
arr = deque([i+1 for i in range(n)])
ans = []
print("<",end='')
while arr:
    for i in range(k-1):
        arr.append(arr.popleft())
    if len(arr) != 1:
        print(arr.popleft(),end=', ')
    else:
        print(arr.popleft(),end='')
print(">")
