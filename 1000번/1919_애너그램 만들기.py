n = list(input())
chkn = [False for i in range(len(n))]
m = list(input())
chkm = [False for i in range(len(m))]
cnt = 0
de = []
for i in range(len(n)):
    for j in range(len(m)):
        if n[i] == m[j] and chkn[i] == False and chkm[j] == False:
            de.append(n[i])
            chkn[i] = True
            chkm[j] = True
for i in de:
    n.remove(i)
    m.remove(i)

print(len(n)+len(m))
