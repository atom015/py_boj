result = []
Del = ["C","A","M","B","R","I","D","G","E"]
n = list(input())
for i in range(len(n)):
    for j in range(len(Del)):
        if n[i] == Del[j]:
            result.append(n[i])
            break
for i in result:
    for j in n:
        if i == j:
            n.remove(i)
for i in n:
    print(i,end='')
