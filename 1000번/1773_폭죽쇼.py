import sys as s
ip = s.stdin.readline
n,c = map(int,ip().split())
a = []
for i in range(n):
    a.append(int(ip()))
def func():
    cnt = 0
    for i in range(1,c+1):
        for j in a:
            if i % j == 0:
                cnt += 1
                break
    return cnt
print(func())
