from math import *
n,k = map(int,input().split())
print(factorial(n)//(factorial(n-k)*factorial(k)))
