import sys
ip = sys.stdin.readline
n = int(ip())
arr = []
for i in range(n):
    arr.append(int(ip()))
c = arr[-1]
cnt = 1
for i in range(n-1,-1,-1):
    if arr[i] > c:
        c = arr[i]
        cnt += 1
print(cnt)
