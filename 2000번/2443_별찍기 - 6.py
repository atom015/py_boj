n = int(input())
minus = 1
for i in range(n):
    print(" "*i+"*"*(2*n-minus))
    minus += 2
