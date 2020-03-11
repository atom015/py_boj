n = int(input())
star = 1
for i in range(n):
    print("*"*star)
    star += 1
star -= 1
for i in range(n-1):
    star -= 1
    print("*"*star)
