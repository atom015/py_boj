n = int(input())
t,p = [0],[0]
d = [0 for i in range(n+2)]
ret = 0
for i in range(n):
    a,b = map(int,input().split())
    t.append(a)
    p.append(b)
for i in range(1,n+2):
    for j in range(1,i):
        d[i] = max(d[i], d[j])
        if j+t[j] == i:
            d[i] = max(d[j]+p[j],d[i])
print(max(d))
