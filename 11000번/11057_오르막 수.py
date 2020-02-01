n = int(input())
d = [[0]*10 for i in range(n)]
d[0] = [1,1,1,1,1,1,1,1,1,1]
for i in range(1,n):
    tmp = sum(d[i-1])
    d[i][0] = tmp
    for j in range(1,10):
        d[i][j] = tmp-d[i-1][j-1]
        tmp -= d[i-1][j-1]
print(sum(d[n-1])%10007)
