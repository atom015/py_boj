n = list(map(int,input()))[::-1]
for i in range(len(n)):
    if i != len(n)-1:
        if n[i] >= 5:
            n[i] = 0
            n[i+1] +=1
    if n[i] < 5 and i != len(n)-1:
        n[i] = 0
s = ""
for i in n[::-1]:
    s += str(i)
print(int(s))
