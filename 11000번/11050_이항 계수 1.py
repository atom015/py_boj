n,k = map(int,input().split())
def Fact(n):
    mul = 1
    for i in range(1,n+1):
        mul *= i
    return mul
print(int(Fact(n) / (Fact(k)*Fact(n-k))))
