import math
n = math.factorial(int(input()))
n = str(n)[::-1]
cnt = 0
for i in n:
    if i == "0":
        cnt += 1
    else:
        break
print(cnt)
