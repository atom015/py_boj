s = 0
for i in range(int(input())):
    n = input()
    tmp = int(n[-1])
    s += int(n[0:-1])**tmp
print(s)
