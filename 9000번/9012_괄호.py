for i in range(int(input())):
    vps = list(input())
    while True:
        if bool(vps) == False:
            print("YES")
            break
        if vps[0] == ")":
            print("NO")
            break
        elif vps[len(vps)-1] == "(":
            print("NO")
            break
        else:
            vps.remove("(")
            vps.remove(")")