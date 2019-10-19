a = sorted(list(int(input()) for i in range(int(input()))))
ans = a[0]
c = 1
cnt = 1
for i in range(1,len(a)):
    if a[i] ==  a[i-1]:
        cnt += 1
    else:
        cnt = 1
    if c < cnt:
        c = cnt
        ans = a[i]
print(ans)
#가장 많이나온숫자에 a[i]값을 출력하는 문제였다.
