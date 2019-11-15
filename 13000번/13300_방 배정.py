n, k = map(int, input().split())
room = 0
cls = [[] for i in range(6)]
for i in range(n):
    s, y = map(int, input().split())
    cls[y - 1].append(s)
for v in cls:
    girl, boy = 0, 0
    for i in v:
        if girl == k:
            room += 1
            girl = 0

        if boy == k:
            room += 1
            boy = 0

        girl += 1 if i == 0 else 0
        boy += 1 if i == 1 else 0

    room += 1 if girl >= 1 else 0
    room += 1 if boy >= 1 else 0
print(room)
