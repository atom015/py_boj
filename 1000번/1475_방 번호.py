import math
li = list(map(int,input()))
chk = [0]*9
for i in li:
    if i == 6 or i == 9:
        chk[5] += 0.5
    else:
        chk[i] += 1
print(math.ceil(max(chk)))
