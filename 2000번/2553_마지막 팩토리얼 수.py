from math import factorial
n = int(input())
fa = factorial(n)
while 1:
    if fa % 10 != 0:
        print(fa%10)
        break
    fa //= 10
