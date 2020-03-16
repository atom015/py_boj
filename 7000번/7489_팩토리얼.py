from math import factorial
import sys
ip = sys.stdin.readline
for i in range(int(ip())):
    n = int(ip())
    n = factorial(n)
    while 1:
        if n % 10 != 0:
            print(n%10)
            break
        n //= 10
