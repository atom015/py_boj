n = int(input())
num = list(int(input()) for i in range(n))
num = sorted(num)

for i in range(len(num)):
    print(num[i])
