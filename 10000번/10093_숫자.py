a,b = map(int,input().split())
if a > b:
    a,b = b,a
if a != b:
    print(b-a-1)
    print(*range(a+1,b))
else:
    print(0)
