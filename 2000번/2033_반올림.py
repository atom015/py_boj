n = int(input())
t = 1
while n > t*10:
    n += 5*t
    t *= 10
    n -= n%t
print(n)
