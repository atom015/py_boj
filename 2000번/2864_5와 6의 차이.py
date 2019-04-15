a,b = input().split()
def max(a,b):
    max = 0
    a = a.replace('5','6')
    b = b.replace('5','6')
    return int(a) + int(b)
def min(a,b):
    min = 0
    a = a.replace('6','5')
    b = b.replace('6','5')
    return int(a) + int(b)
print(min(a,b),max(a,b))