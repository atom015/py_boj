int(input())
a = list(input())
if a.count("A") > a.count("B"):
    print("A")
elif a.count("B") > a.count("A"):
    print("B")
else:
    print("Tie")
