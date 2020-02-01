n = int(input())
cnt = 1
blank = n-1
for i in range(n):
    print(" "*blank+"*"*cnt)
    blank -= 1
    cnt += 2
blank += 2
cnt -= 4
for i in range(n-1):
    print(" "*blank+"*"*cnt)
    blank += 1
    cnt -= 2
