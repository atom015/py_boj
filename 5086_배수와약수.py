while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    avg = b % a
    mul = a // b
    if avg == 0:
        print("factor")
    elif mul * b == a:
        print("multiple")
    else:
        print("neither")
