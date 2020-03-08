import sys
ip = sys.stdin.readline
for i in range(int(ip())):
    a,b = map(int,ip().split())
    ans = pow(a,b,10)
    print(10 if ans == 0 else ans)
