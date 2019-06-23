import sys
n = int(sys.stdin.readline())
nli = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mli = list(map(int,sys.stdin.readline().split()))
for i in mli:
    if i in nli:
        print(1)
    else:
        print(0)
#원래 이분탐색으로 해야하는데 일부로 sys.stdin.readline()애 pypy3으로 해서 시간초과를 없앴다.
