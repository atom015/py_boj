n = int(input())
star = n*2-1
fs = 0
for i in range(n):
    print(" "*fs+"*"*star)
    fs += 1
    star -= 2
fs -= 1
star += 2
for i in range(n-1):
    fs -= 1
    star += 2
    print(" "*fs+"*"*star)
