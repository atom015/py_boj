t = int(input())
n = sorted(list(map(int,input().split())))
stack = []
for i in range(t):
    if i == 0:
        stack.append(n[i])
    else:
        s = 0
        for j in range(i+1):
            s += n[j]
        stack.append(s)
print(sum(stack))