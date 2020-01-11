n = ["0"]+list(input())
m = ["0"]+list(input())
d = [[0 for i in range(len(n))] for i in range(len(m))]
for i in range(1,len(m)):
    for j in range(1,len(n)):
        if m[i] == n[j]:
            d[i][j] = d[i-1][j-1]+1
        else:
            d[i][j] = max(d[i][j-1],d[i-1][j])
ans = 0
for i in d:
    ans = max(ans,max(i))

print(ans)
