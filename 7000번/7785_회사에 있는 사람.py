a = set()
for i in range(int(input())):
    n,chk = input().split()
    if chk == "enter":a.add(n)
    else:a.remove(n)
for i in sorted(a)[::-1]:
    print(i)
