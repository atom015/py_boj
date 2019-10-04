n = int(input())
a = list(input())
idx = {"A":0,"G":1,"C":2,"T":3}
base = [["A","C","A","G"],
        ["C","G","T","A"],
        ["A","T","C","G"],
        ["G","A","G","T"]]
while 1:
    if len(a) == 1:
        print("".join(a))
        break
    an = idx[a.pop()]
    an1 = idx[a.pop()]
    a.append(base[an][an1])
