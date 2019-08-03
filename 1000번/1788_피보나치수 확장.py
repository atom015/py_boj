def main():
    n = int(input())
    if n == 0:
        print("0\n0")
        return
    chk = True
    if n < 0:
        n = abs(n)
        chk = False
    a,b = 0,1
    for i in range(2,n+1):
        tmp = b
        b = (a+b) % 1000000000
        a = tmp
    if chk == False and n % 2 == 0:
        print(-1)
    else:
        print(1)
    print(b)
main()
