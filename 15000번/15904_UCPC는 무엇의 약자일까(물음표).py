n = input()
cnt = 0
for i in n:
    if cnt == 0 and i == "U":
        cnt += 1
    if cnt == 1 and i == "C":
        cnt += 1
    if cnt == 2 and i == "P":
        cnt += 1
    if cnt == 3 and i == "C":
        cnt += 1
if cnt == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")
