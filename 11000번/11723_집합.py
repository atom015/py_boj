sets = set()
def chk(x):
    if int(x) in sets:
        return 1
    else:
        return 0
def add(x):
    if int(x) not in sets:
        sets.add(int(x))
def remove(x):
    if len(sets) != 0:
        sets.remove(int(x))
def toggle(x):
    if int(x) in sets:
        sets.remove(int(x))
    else:
        sets.add(int(x))
for i in range(int(input())):
    n = input()
    if n[:3] == "add":
        add(n[4:])
    elif n[:5] == "check":
        print(chk(n[6:]))
    elif n[:6] == "remove":
        remove(n[7:])
    elif n[:6] == "toggle":
        toggle(n[7:])
    elif n == "all":
        sets = set(i for i in range(1,21))
    elif n == "empty":
        sets = set()
