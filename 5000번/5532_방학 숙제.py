li = [int(input()) for i in range(5)]#방학,수학 총,국어 총,국어최대,수학최대
minus_day = 0
while 1:
    if li[1] <= 0 and li[2] <= 0:
        break
    li[1] -= li[3]
    li[2] -= li[4]
    minus_day += 1
print(li[0]-minus_day)
