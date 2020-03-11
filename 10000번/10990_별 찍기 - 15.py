n = int(input())
ms = 1
fs = n-1
print(" "*fs+"*")
fs -= 1
for i in range(n-1):
    print(" "*fs+"*"+" "*ms+"*")
    fs -= 1
    ms += 2
