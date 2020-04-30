def digital(n):
    n = list(str(n))
    n = [int(i) for i in n]
    n = sum(n)
    while 2 <= len(str(n)):
        n = list(str(n))
        n = [int(i) for i in n]
        n = sum(n)
    return n
while 1:
    n = int(input())
    if n == 0:
        break
    print(digital(n))
