from collections import deque
import sys
ip = sys.stdin.readline
q = deque([])
for i in range(int(ip())):
    n = ip().strip()
    if n[0:4] == "push":
        q.append(int(n[5:]))
    else:
        if n == "pop":
            if not len(q):
                print(-1)
            else:
                print(q.popleft())
        elif n == "size":
            print(len(q))
        elif n == "front":
            if not len(q):
                print(-1)
            else:
                print(q[0])
        elif n == "empty":
            if not len(q):
                print(1)
            else:
                print(0)

        else:
            if not len(q):
                print(-1)
            else:
                print(q[-1])
