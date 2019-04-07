s = input()
n = []
for i in range(len(s)):
    n.append(s[i:])
n.sort()
for i in n:
    print(i)
