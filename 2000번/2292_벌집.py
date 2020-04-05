n = int(input())
ret = 1
tmp = 0
ans = 1
while 1:
    if n <= ans:
        print(ret)
        break
    tmp += 6
    ans += tmp
    ret += 1
