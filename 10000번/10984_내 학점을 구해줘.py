for i in range(int(input())):
    n = int(input())
    s = 0
    s1 = 0
    for i in range(n):
        a,b = map(float,input().split())
        s += a
        s1 += a*b
    print(int(s),round(s1/s,1))
