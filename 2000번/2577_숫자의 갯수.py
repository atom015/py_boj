n = [0 for i in range(10)]
a = int(input())
b = int(input())
c = int(input())
temp = [int(i) for i in list(str(a*b*c))]
for i in range(10):
    for j in range(len(temp)):
        if temp[j] == i:
            n[i] += 1
    print(n[i])
