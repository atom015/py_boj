a = []
for i in range(int(input())):
    s = input().split()
    a.append((int(s[1]),int(s[2]),int(s[3]),s[0]))
stu.sort(key=lambda x: (-x[0],x[1],-x[2],x[3]))
for i in a:
    print(i[3])
