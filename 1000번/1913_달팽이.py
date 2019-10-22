n = int(input())
m = int(input())

def snail(n):
    a = [[0 for i in range(n)] for i in range(n)]
    i,j,num = -1,0,n*n
    chk = 1
    while n > 0:
        for _ in range(n):
            i += chk
            a[i][j] = num
            num -= 1
        n -= 1
        if n == 0:break
        for _ in range(n):
            j += chk
            a[i][j] = num
            num -= 1
        chk *= -1
    return a
a = snail(n)
for i in a:
    for j in i:
        print(j,end=' ')
    print()
for i in range(n):
    for j in range(n):
        if a[i][j] == m:
            print(i+1,j+1)
