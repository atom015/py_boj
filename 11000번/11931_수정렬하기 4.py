import sys
ip = sys.stdin.readline
arr = []
for i in range(int(ip())):
    arr.append(int(ip()))
for i in sorted(arr)[::-1]:
    print(i)
