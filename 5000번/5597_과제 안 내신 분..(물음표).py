li = sorted(list(int(input()) for i in range(28)))
for i in range(1,31):
    if i not in li:
        print(i)
