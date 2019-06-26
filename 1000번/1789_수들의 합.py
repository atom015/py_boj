n = int(input())
sum = 0
num = 1
while 1:
    sum += num
    if sum > n:
        print(num-1)
        break
    num += 1
