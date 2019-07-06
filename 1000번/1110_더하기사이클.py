cnt = 0
n = input()
c = [int(i) for i in n]
c = str(c[-1])+str(sum(c))[-1]
while 1:
    cnt += 1
    if int(c) == int(n):
        break
    c = [int(i) for i in c]
    c = str(c[-1])+str(sum(c))[-1]
print(cnt)
