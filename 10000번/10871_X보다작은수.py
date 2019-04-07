n,x = map(int,input().split())
a = list(map(int,input().split()))
temp = []
for i in range(len(a)):
    if a[i] < x:
        temp = a[i]
        print(temp,end=' ')
    else:continue
