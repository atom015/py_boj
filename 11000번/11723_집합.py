import sys
ip = sys.stdin.readline
v = [False for i in range(21)]
for _ in range(int(ip())):
    s = ip().strip()
    if s == "empty":
        v = [False for i in range(21)]
    elif s == "all":
        v = [True for i in range(21)]
    else:
        s,x = s.split()
        if s == "add":
            v[int(x)] = True
        elif s == "remove":
            v[int(x)] = False
        elif s == "check":
            if v[int(x)] == True:
                print(1)
            else:
                print(0)
        else:
            if v[int(x)] == True:
                v[int(x)] = False
            else:
                v[int(x)] = True
