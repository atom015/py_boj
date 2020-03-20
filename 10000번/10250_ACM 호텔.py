for i in range(int(input())):
    h,w,n = map(int,input().split())
    num,ho,cnt = 1,101,2
    while num != n:
        if ho//100 == h:
            ho = 100+cnt
            cnt += 1
        else:
            ho += 100
        num += 1
    print(ho)
