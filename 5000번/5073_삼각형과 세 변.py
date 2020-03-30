while 1:
    a,b,c = map(int,input().split())
    if a == b == c == 0:break
    s = sorted([a,b,c])
    if sum(s[:-1]) <= s[2]:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a != b != c != a:
        print("Scalene")
    else:
        print("Isosceles")
