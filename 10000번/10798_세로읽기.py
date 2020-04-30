n = []
result = []
max = 0
for i in range(5):
	n.append(list(input()))
for i in range(len(n)):
    if max < len(n[i]):
        max = len(n[i])
for i in range(len(n)):
    if len(n[i]) != max:
        for l in range(max-len(n[i])):
            n[i].append(None)
for i in range(max):
    for j in range(len(n)):
        if n[j][i] == None:
            continue
        else:
            result.append(n[j][i])
for i in result:
    print(i,end='')
