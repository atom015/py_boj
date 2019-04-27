for i in range(int(input())):
    a,b = list(map(int,input().split()))
    n1,n2 = a,b
    while True:
        if b != 0:
            r = a%b
            a = b
            b = r
        else:
            print(int(n1*n2/a))
            break