from math import *
n,w,h = map(int,input().split())
for i in range(n):
    t = int(input())
    if t > w and t > h and t > sqrt((w**2)+(h**2)):
        print("NE")
    else:
        print("DA")
