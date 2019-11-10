for i in range(100):
    try:
        n = input()
    except:
        break
    lo,up,nu,sp = 0,0,0,0
    for i in n:
        if i.isdigit():
            nu += 1
        elif i.isupper():
            up += 1
        elif i.islower():
            lo += 1
        elif i == " ":
            sp += 1
    print(lo,up,nu,sp)