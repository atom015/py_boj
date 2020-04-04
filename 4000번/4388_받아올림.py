while 1:
    a,b = input().split()
    if a == b == '0':break
    s = str(int(a)+int(b))
    a = a.zfill(len(s))
    b = b.zfill(len(s))
    ret = 0
    arr = [(int(a[i])+int(b[i]))%10 for i in range(len(s))]
    for i in range(len(s)):
        if arr[i] != int(s[i]):
            ret += 1
    print(ret)
