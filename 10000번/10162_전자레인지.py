second = int(input())
if second % 10 != 0:print("-1")
else:
    A = second / 300
    second %= 300
    B = second / 60
    second %= 60
    C = second / 10
    second %= 10
    print(int(A),int(B),int(C))
