from collections import deque
import sys
ip = sys.stdin.readline
lst = deque(list(ip().strip()))
rst = deque([])
for i in range(int(ip())):
    cmd = ip().strip()
    if cmd[0] == 'L':
        if len(lst):
            rst.appendleft(lst.pop())
    elif cmd[0] == 'D':
        if len(rst):
            lst.append(rst.popleft())
    elif cmd[0] == 'B':
        if len(lst):
            lst.pop()
    else:
        lst.append(cmd[2])
for i in lst+rst:
    print(i,end='')
