n,k = map(int,input().split())
room = 0
cls = [[] for i in range(6)]
for i in range(n):
    s,y = map(int,input().split())
    cls[y-1].append(s)
for v in cls:
    girl,boy = 0,0
    for i in v:
        if girl == k:
            room += 1
            girl = 0

        if boy == k:
            room += 1
            boy = 0

        if i == 0:
            girl += 1
        elif i == 1:
            boy += 1
    if girl >= 1:
        room += 1
    if boy >= 1:
        room += 1
print(room)
