n = int(input())
num = sorted(list(int(input()) for i in range(n)))
for i in range(len(num)):
    print(num[i])
