t = int(input())
group = []
chk = 0
for i in range(t):
    group.append(input())
for i in range(t):
    g_chk = []
    for j in range(len(group[i])):
        if len(group[i]) == 1:
            break
        elif j == 0:
            g_chk.append(group[i][j])
        else:
            if group[i][j-1] != group[i][j] and group[i][j] in g_chk:
                chk += 1
                break
            else:
                g_chk.append(group[i][j])
print(len(group)-chk)