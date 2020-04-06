n = input()
if n[0:2] == "0x":
    print(int(n,16))
elif n[0] == "0":
    print(int(n,8))
else:
    print(n)
