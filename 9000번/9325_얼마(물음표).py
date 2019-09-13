for i in range(int(input())):
    s = int(input())
    for i in range(int(input())):
        q,p = map(int,input().split())
        s += q*p
    print(s)
