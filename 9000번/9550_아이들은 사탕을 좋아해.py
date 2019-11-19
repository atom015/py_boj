t = int(input())
for i in range(t):
    cnt = 0
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    for i in a:
        cnt += i//k
    print(cnt)
