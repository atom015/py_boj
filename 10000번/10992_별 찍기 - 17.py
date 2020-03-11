n = int(input())
if n == 1:
    print("*")
else:
    fs = n-1
    ms = 1
    print(" "*fs+"*")
    fs -= 1
    for i in range(n-2):
        print(" "*fs+"*"+" "*ms+"*")
        fs -= 1
        ms += 2
    print("*"*((n*2)-1))
