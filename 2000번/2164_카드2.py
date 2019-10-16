import sys,collections
ip = sys.stdin.readline
n = int(ip())
a = collections.deque([i for i in range(1,n+1)])
def func():
    while len(a) != 1:
        a.popleft()
        a.append(a.popleft())
func()
print(a[0])
