for i in range(3):
    li = list(map(int,input().split()))
    if li.count(0) == 1 and li.count(1) == 3:
        print("A")
    elif li.count(0) == 2 and li.count(1) == 2:
        print("B")
    elif li.count(0) == 3 and li.count(1) == 1:
        print("C")
    elif li.count(0) == 4:
        print("D")
    elif li.count(1) == 4:
        print("E")
