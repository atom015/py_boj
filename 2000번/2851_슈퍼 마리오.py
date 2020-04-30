li = [int(input()) for i in range(10)]
sum = 0
for i in range(10):
    afs = sum + li[i]
    if afs >= 100:
        if afs - 100 <= 100 - sum:
            print(afs)
        else:
            print(sum)
        exit()
    sum = afs
print(sum)
