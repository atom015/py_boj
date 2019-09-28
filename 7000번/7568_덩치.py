n = int(input())
a = []
for i in range(n):
    t,t1 = map(int,input().split())
    a.append([t,t1,1])
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            a[i][2] += 1
for i in a:
    print(i[2],end=' ')
