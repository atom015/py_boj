s = list(input())
def chk1():
    for i in s:
        if i != "2" and i != "0" and i != "1" and i != "8":
            return False
    return True
if chk1():
    if s.count("2") and s.count("0") and s.count("1") and s.count("8"):
        if s.count("2") == s.count("0") == s.count("1") == s.count("8"):
            print(8)
        else:
            print(2)
    else:
        print(1)
else:
    print(0)
