cnt = 0
def S(n):
    s = 0
    while n:
        s += n%10
        n //= 10
    return s
for i in range(1,int(input())+1):
    if i % S(i) == 0:
        cnt += 1
print(cnt)
