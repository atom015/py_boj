n = int(input())
def type_chk():
    global n
    if type(n) == float:
        n = int(n)
while 1:
    compare = input()
    if compare == "=":
        break
    m = int(input())
    if compare == "+":
        type_chk()
        n += m
    elif compare == "-":
        type_chk()
        n -= m
    elif compare == "*":
        type_chk()
        n *= m
    elif compare == "/":
        type_chk()
        n /= m
print(n)
