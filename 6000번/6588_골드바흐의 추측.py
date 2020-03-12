import sys
ip = sys.stdin.readline
MAX = 1000000
prime = [False for i in range(MAX+1)]
a = [True]+[False]*(MAX)
for i in range(2,MAX+1):
    if not a[i]:
        for j in range(i*i, MAX+1, i):
            a[j] = True
for i in range(3,MAX):
    if a[i] == False:
        prime[i] = True
while 1:
    n = int(ip())
    if n == 0:break
    for i in range(2,MAX+1):
        if i > n:break
        if prime[i]:
            tp = n-i
            if prime[tp]:
                print("{} = {} + {}".format(n,i,tp))
                break
