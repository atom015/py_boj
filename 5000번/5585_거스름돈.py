change = [500,100,50,10,5,1]
n = 1000-int(input())
cnt = 0
for i in change:
    if n == 0:
        break
    cnt += n // i
    n %= i
print(cnt)
