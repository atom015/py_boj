li = [list(input()) for i in range(8)]
chk = []
cnt = 0
def location(li):
    for i in range(0,7,2):
        for j in range(0,7,2):
            li.append([i,j])
    for i in range(1,8,2):
        for j in range(1,8,2):
            li.append([i,j])
location(chk)
for i in range(len(chk)):
    if li[chk[i][0]][chk[i][1]] == "F":
        cnt += 1
print(cnt)
