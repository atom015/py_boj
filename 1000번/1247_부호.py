import sys
ip = sys.stdin.readline
for i in range(3):
    s = 0
    for j in range(int(ip())):
        s += int(ip())
    print("0" if s == 0 else ("-" if s < 0 else "+"))
