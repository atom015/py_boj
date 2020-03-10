n = int(input())
mid_s = n*2-2
star = 1
for i in range(n):
    print("*"*star+" "*mid_s+"*"*star)
    star += 1
    mid_s -= 2
star -= 1
mid_s += 2
for i in range(n-1):
    mid_s += 2
    star -= 1
    print("*"*star+" "*mid_s+"*"*star)
