Ysum = 0
Ksum = 0
T = int(input())
for i in range(T):
    for j in range(9):
        Y,K = map(int,input().split())
        Ysum += Y
        Ksum += K
    if Ysum > Ksum:
        print("Yonsei")
    elif Ysum == Ksum:
        print("Draw")
    elif Ysum < Ksum:
        print("Korea")
