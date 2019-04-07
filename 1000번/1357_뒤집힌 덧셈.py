x,y = input().split()
def Rint(x,y):
    sum = str(int(x[::-1]) + int(y[::-1]))
    return sum
def Rev(n):
    reverse = n[::-1]
    return int(reverse)
print(Rev(Rint(x,y)))
