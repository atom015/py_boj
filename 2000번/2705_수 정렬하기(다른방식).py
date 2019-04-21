n = []
for i in range(int(input())):
    n.append(int(input()))

for i in range(len(n)):
    for j in range(len(n)):
        tmp_i = n[i]
        tmp_j = n[j]
        if i != j:
            if n[i] < n[j]:
                n[i] = tmp_j
                n[j] = tmp_i
for i in n:
    print(i)