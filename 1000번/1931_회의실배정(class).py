import sys
ip = sys.stdin.readline
class Time:
    def __init__(self,s,e):
        self.s = s
        self.e = e
n = int(ip())
arr = []
for i in range(n):
    a,b = map(int,ip().split())
    arr.append(Time(a,b))
arr.sort(key=lambda x:(x.e,x.s))
cnt = 1
e = arr[0].e
for i in range(1,n):
    if e <= arr[i].s:
        e = arr[i].e
        cnt += 1
print(cnt)
