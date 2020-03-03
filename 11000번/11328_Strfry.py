for i in range(int(input())):
    a,b = input().split()
    if len(a) != len(b):
        print("Impossible")
        continue
    chk = False
    a,b = sorted(list(a)),sorted(list(b))
    for i in range(len(a)):
        if a[i] != b[i]:
            print("Impossible")
            chk = True
            break
    if not chk:
        print("Possible")
