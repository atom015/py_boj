for i in range(int(input())):
    a = list(input().split())
    fl = float(a[0])
    del a[0]
    for j in range(len(a)):
        if a[j] == "@":
            fl *= 3
        elif a[j] == "#":
            fl -= 7
        elif a[j] == "%":
            fl += 5
        else:
            pass
    print("%.2f" % fl)
