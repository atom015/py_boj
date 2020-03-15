n = int(input())
while n > 0:
    s = list(str(n))
    if len(s) == s.count("7")+s.count("4"):
        print("".join(s))
        break
    n -= 1
