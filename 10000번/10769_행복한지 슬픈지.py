s = input()
happy,sad = s.count(":-)"),s.count(":-(")
if happy == sad == 0:
    print("none")
elif happy == sad:
    print("unsure")
elif happy > sad:
    print("happy")
else:
    print("sad")
