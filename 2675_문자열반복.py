for i in range(int(input())):
    a = list(input().split())
    st = list(a[1])
    temp = int(a[0])
    for k in range(len(st)):
        print(temp * str(st[k]),end='')
    print()
