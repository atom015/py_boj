n = int(input())
fs = n-1
star = 1
for i in range(n):
    print(" "*fs+"* "*star)
    fs -= 1
    star += 1
