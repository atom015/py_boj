n = int(input())
li = list(input())
def Lchange():
    while "L" in li:
        ix = li.index("L")
        li.remove("L")
        li.insert(ix,"LL")
        li.remove("L")
Lchange()
li = "*".join(li)
result = li.count("*")+2
if result > n:
    print(n)
else:
    print(result)
