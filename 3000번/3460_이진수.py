for i in range(int(input())):
    n = int(input())
    idx = 0
    while n != 0:
        if n&1:
            print(idx,end=" ")
        idx+=1
        n >>= 1
