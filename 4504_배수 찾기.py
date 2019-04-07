t = int(input())
while True:
    n = int(input())
    if n == 0:
        break
    if n % t == 0:
        print("{} is a multiple of {}.".format(n,t))
    else:
        print("{} is NOT a multiple of {}.".format(n,t))
