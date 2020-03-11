from math import factorial
n,m = map(int,input().split())
def tc(n):
    two = 0
    i = 2
    while i <= n:
        two += n//i
        i *= 2
    return two
def fc(n):
    five = 0
    i = 5
    while i <= n:
        five += n//i
        i *= 5
    return five
t = [tc(n),tc(m),tc(n-m)]
f = [fc(n),fc(m),fc(n-m)]
print(min(t[0]-t[1]-t[2],f[0]-f[1]-f[2]))
