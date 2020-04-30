n,k,m = map(int,input().split())
money = (n*k)-m
if money < 0:
    print(0)
elif money > 0:
    print(money)
