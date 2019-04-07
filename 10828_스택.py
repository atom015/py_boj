Stack = []
for i in range(int(input())):
    n = input()
    if n[:4] == "push":
        Stack.append(int(n[5:]))
    elif n == "top":
        if len(Stack) >= 1:
             print(Stack[len(Stack)-1])
        else:
            print(-1)
    elif n == "pop":
        if len(Stack) >= 1:
            print(Stack.pop())
        else:
            print(-1)
    elif n == "size":
        print(len(Stack))
    elif n == "empty":
        if len(Stack) == 0:
            print(1)
        else:
            print(0)
