a,b = input().split()
aix,bix = -1,-1
chk = False
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            aix,bix = i,j
            break
    if aix >= 0 and bix >= 0:
        break
for i in range(len(b)):
    for j in range(len(a)):
        if j == aix and i != bix:
            print(b[i],end='')
        elif i == bix:
            for k in range(len(a)):
                print(a[k],end='')
            break
        else:
            print(".",end='')
    print()
