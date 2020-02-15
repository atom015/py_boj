n = int(input())
if n <= 5:
    print(n)
elif n % 4 == 0:
    p = n//4
    if p % 2 == 0:
        print(2)
    else:
        print(4) #p - 층
else:
    p = 4*(n//4+1)-n #p - 차이
    if (n//4+1) % 2 == 0:
        print(2+p)
    else:
        print(4-p)
