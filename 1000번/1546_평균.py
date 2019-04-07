n = int(input())
a = list(map(int,input().split()))
temp = max(a)
avg = 0
sum = 0
for i in range(len(a)):
    sum += a[i] / temp * 100
avg = sum / n
print(avg)
