s = 0
a = list(map(int,input().split()))
for i in a:
    s += i**2
print(s%10)
