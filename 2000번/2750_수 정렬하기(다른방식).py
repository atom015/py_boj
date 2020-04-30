n = []
for i in range(int(input())):
    n.append(int(input()))

for i in range(len(n)):
    for j in range(len(n)):
        if i != j:
            if n[i] < n[j]:
                n[i],n[j] = n[j],n[i]
for i in n:
    print(i)
