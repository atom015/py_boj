li = [int(input()) for i in range(5)]
chk = []
for i in range(3):
    for j in range(3,5):
        if i != j:
            chk.append(li[i]+li[j]-50)
print(min(chk))
