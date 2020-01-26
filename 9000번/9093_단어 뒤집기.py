import sys
ip = sys.stdin.readline
for i in range(int(ip())):
    for i in ip().split():
        print(i[::-1],end=' ')
    print()
