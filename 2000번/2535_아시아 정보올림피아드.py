N = int(input())
chk = [0]*N
arr = []
ans = []

for i in range(N):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:-x[2])

for con,nu,po in arr:
    if len(ans) != 3 and chk[con-1] < 2:
        ans.append([con,nu])
        chk[con-1] += 1

for i in ans:
    print(*i)
