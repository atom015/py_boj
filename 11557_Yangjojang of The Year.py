m = 0
for i in range(int(input())):
    t = int(input())
    sn = [0 for i in range(1,t+1)]
    s = [0 for i in range(1,t+1)]
    for j in range(t):
        sn[j],s[j] = input().split()
    for i in range(len(s)):
        if m < int(s[i]):
            m = int(s[i])
    for i in range(len(s)):
        if m == int(s[i]):
            print(sn[i])
