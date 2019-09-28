i = 666
n = int(input())
t = 0
while 1:
    if t == n:
        break
    if str(i).find("666") != -1:
        num = i
        t += 1
    i += 1
print(num)
