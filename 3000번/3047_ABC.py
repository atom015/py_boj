t = sorted(list(map(int,input().split())))
abc = list(input())
for i in range(3):
    if abc[i] == "A":
        print(t[0],end=' ')
    elif abc[i] == "B":
        print(t[1],end=' ')
    elif abc[i] == "C":
        print(t[2],end=' ')
