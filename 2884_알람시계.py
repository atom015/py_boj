H,M = map(int,input().split())
if H == 0:
    H = 23
    M -= 45
    print(H,60 - abs(M))
elif (M - 45) < 0:
    H -= 1
    M -= 45
    print(H,60 - abs(M))
else:
    print(H,M-45)
