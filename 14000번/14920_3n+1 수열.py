n = int(input())
cnt = 0
def C(n):
    global cnt
    cnt += 1
    if n == 1:
        return
    if n % 2 == 0:
        C(n//2)
    else:
        C(3*n+1)
C(n)
print(cnt)