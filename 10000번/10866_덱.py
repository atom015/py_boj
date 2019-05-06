Deque = []
for i in range(int(input())):
    n = input()
    if n[:10] == "push_front":
        Deque.insert(0,int(n[11:]))
    elif n[:9] == "push_back":
        Deque.append(int(n[10:]))
    elif n == "front":
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[0])
    elif n == "back":
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque[len(Deque)-1])
    elif n == "size":
        print(len(Deque))
    elif n == "empty":
        if len(Deque) == 0:
            print(1)
        else:
            print(0)
    elif n == "pop_front":
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque.pop(0))
    elif n == "pop_back":
        if len(Deque) == 0:
            print(-1)
        else:
            print(Deque.pop())