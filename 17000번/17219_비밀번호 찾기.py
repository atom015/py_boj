import sys
ip = sys.stdin.readline
n,m = map(int,ip().split())
dic = {}
for i in range(n):
    a,b = ip().split()
    dic[a] = b
for i in range(m):
    s = input()
    print(dic[s])
