n = int(input())
a = [input() for _ in range(n)]
tmp = []

def Sum(st):
    s = 0
    for i in st:
        if i.isdigit() == True:
            s += int(i)
    return s


for i in range(n):
    for j in range(n):
        if i != j:
            if len(a[i]) > len(a[j]):
                a[i],a[j] = a[j],a[i]
            elif len(a[i]) == len(a[j]):
                t1,t2 = Sum(a[i]),Sum(a[j])
                if t1 > t2:
                    a[i],a[j] = a[j],a[i]
                elif t1 == t2:
                    arr = sorted([a[i],a[j]])
                    a[i],a[j] = arr[0],arr[1]
for i in reversed(a):
    print(i)