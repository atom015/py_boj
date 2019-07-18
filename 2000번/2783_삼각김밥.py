a,b = map(int,input().split())
n = int(input())
ab = a / b * 1000
for i in range(n):
    x,y = map(int,input().split())
    xy = x / y * 1000
    if ab > xy:
        ab = xy
print("%.2f" % ab)
