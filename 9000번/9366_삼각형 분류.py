for i in range(int(input())):
    a,b,c = sorted(map(int,input().split()))
    if a+b <= c:
        ret = "invalid!"
    elif a == b == c:
        ret = "equilateral"
    elif a == b or b == c or a == c:
        ret = "isosceles"
    else:
        ret = "scalene"
    print("Case #{}: {}".format(i+1,ret))
