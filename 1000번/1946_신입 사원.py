from sys import *
ip = stdin.readline
for i in range(int(ip())):
    N = int(ip())
    arr = [0]*(N+1)
    for i in range(N):
        a,b = map(int,ip().split())
        arr[a] = b
    cnt = 1
    c = arr[1]
    for i in range(2,N+1):
        t = arr[i]
        if c >= t:
            cnt += 1
            c = t
    print(cnt)
