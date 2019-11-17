for i in range(100):
    try:
        n = input()
        while "BUG" in n:
            n = n.replace("BUG","")
        print(n)
    except:
        break
