for i in range(int(input())):
    a = list(input().split())
    b = list(input().split())
    del a[0],b[0]
    if a.count('4') < b.count('4'):
        print("B")
    elif a.count('4') > b.count('4'):
        print("A")
    else:
        if a.count('3') < b.count('3'):
            print("B")
        elif a.count('3') > b.count('3'):
            print("A")
        else:
            if a.count('2') < b.count('2'):
                print("B")
            elif a.count('2') > b.count('2'):
                print("A")
            else:
                if a.count('1') < b.count('1'):
                    print("B")
                elif a.count('1') > b.count('1'):
                    print("A")
                elif a.count('1') == b.count('1'):
                    print("D")
