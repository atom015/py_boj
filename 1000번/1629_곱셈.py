a,b,c = map(int,input().split())
def calc(a,m,c):
    if m == 0:return 1
    if m % 2 != 0:
        return (calc(a,m-1,c)*a)%c
    half = calc(a,m//2,c)
    return (half*half)%c
print(calc(a,b,c))
