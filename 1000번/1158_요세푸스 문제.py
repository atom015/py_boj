from collections import deque
n,m = map(int,input().split())

q = deque([i+1 for i in range(n)])
print("<",end='')
for i in range(n-1):
    for j in range(m-1):
        q.append(q.popleft())
    print(q.popleft(),end=', ')
print(q.popleft(),end=">")
