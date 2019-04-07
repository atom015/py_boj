for i in range(int(input())):
    n = list(input().split())
    if n[1] == "+":
        if int(n[0]) + int(n[2]) == int(n[-1]):
            print("correct")
        else:
            print("wrong answer")
    elif n[1] == "-":
        if int(n[0]) - int(n[2]) == int(n[-1]):
            print("correct")
        else:
            print("wrong answer")
    elif n[1] == "*":
        if int(n[0]) * int(n[2]) == int(n[-1]):
            print("correct")
        else:
            print("wrong answer")
    elif n[1] == "/":
        if int(n[0]) / int(n[2]) == int(n[-1]):
            print("correct")
        else:
            print("wrong answer")
