import sys
ip = sys.stdin.readline
n = int(ip())
arr = [list(map(int,ip().split())) for i in range(n)]
tmp = [[] for i in range(n)]
ans = [set() for i in range(n)]
for i in range(n):
    for j in range(i,n):
        for k in range(5):
            if arr[i][k] == arr[j][k]:
                ans[i].add(j)
                ans[j].add(i)
MAX = 0
for i in ans:
    MAX = max(MAX,len(i))
ret = []
for i in range(n):
    if MAX == len(ans[i]):
        ret.append(i+1)
print(min(ret))
