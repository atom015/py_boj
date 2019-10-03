def euclid(a,b):
    if b > a:
        tmp = a
        a,b = b,tmp
    while 1:
        if b == 0:
            break
        tmp = a
        a = b
        b = tmp%b
    return a
n,m = map(int,input().split(":"))
ans = euclid(n,m)
print("{}:{}".format(n//ans,m//ans))
