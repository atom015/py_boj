queue = []
for i in range(int(input())):
    n = input()
    if n[:4] == "push":
        queue.append(int(n[5:]))
    elif n == "pop":
        if len(queue) >= 1:
            print(queue.pop(0))
        else:
            print(-1)
    elif n == "size":
        print(len(queue))
    elif n == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif n == "front":
        if len(queue) >= 1:
            print(queue[0])
        else:
            print(-1)
    elif n == "back":
        if len(queue) >= 1:
            print(queue[len(queue)-1])
        else:
            print(-1)
