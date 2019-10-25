n,m = map(int,input().split())
q = [i for i in range(1,n+1)]
print("<",end='')
for i in range(n-1):
    for j in range(m-1):
        q.append(q.pop(0))
    print(q.pop(0),end=', ')
print(q[0],end='>')
