for i in range(int(input())):
    r,e,c = map(int,input().split())
    r += c
    if r < e:
        print("advertise")
    elif r > e:
        print("do not advertise")
    else:
        print("does not matter")
