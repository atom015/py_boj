n = input()
if len(n) == 2:
    cnt = 0
    n1 = n
    while True:
        a = n1[0]
        b = n1[1]
        c = str(int(a) + int(b))
        if len(c) == 2:
            n1 = b+c[1]
            cnt += 1
        else:
            n1 = b+c
            cnt += 1
        if n1 == n:
            break
    print(cnt)
elif len(n) == 1:
    npz = '0'+n
    cnt = 0
    n1 = "0"+n
    while True:
        a = n1[0]
        b = n1[1]
        c = str(int(a) + int(b))
        if len(c) == 2:
            n1 = b+c[1]
            cnt += 1
        else:
            n1 = b+c
            cnt += 1
        if n1 == npz:
            break
    print(cnt)
