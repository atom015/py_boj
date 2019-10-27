n = int(input())
v = list(map(int,input().split()))
ans = [-1 for i in range(n)]
s = []

for i in range(n):
    while len(s) and v[s[-1]] < v[i]:
        ans[s[-1]] = v[i]
        s.pop()
    s.append(i)
for i in ans:
    print(i,end=' ')
