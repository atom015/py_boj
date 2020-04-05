from sys import *
from collections import deque
ip = stdin.readline
for i in range(int(ip())):
    p = ip().strip()
    n = int(ip())
    arr = deque(eval(ip().strip()))
    c,chk = -1,True
    for i in p:
        if i == "R":
            c *= -1
        else:
            if not arr:
                chk = False
                break
            else:
                if c == -1:
                    arr.popleft()
                else:
                    arr.pop()
    if not arr and not chk:
        print("error")
        continue
    if c == 1:
        arr.reverse()
    print("[",end='')
    print(*arr,sep=',',end='')
    print("]")
