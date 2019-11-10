n,m = map(int,input().split())
A = [list(input()) for _ in range(n)]
B = [list(input()) for _ in range(n)]
i = 0
while i <= n-1:
    j = 0
    while j <= m*2-1:
        A[i].insert(j,A[i][j])
        j += 2
    i += 1
if A == B:
    print("Eyfa")
else:
    print("Not Eyfa")