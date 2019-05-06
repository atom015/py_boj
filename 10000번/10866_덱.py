Deque = []
def PuF():
    global Deque
    Deque.insert(0,int(n[11:]))
def PuB():
    global Deque
    Deque.append(int(n[10:]))
def front():
    global Deque
    if len(Deque) == 0:
        return -1
    else:
        return Deque[0]
def back():
    global Deque
    if len(Deque) == 0:
        return -1
    else:
        return Deque[len(Deque)-1]
def size():
    global Deque
    return len(Deque)
def empty():
    global Deque
    if len(Deque) == 0:
        return 1
    else:
        return 0
def PoF():
    global Deque
    if len(Deque) == 0:
        return -1
    else:
        return Deque.pop(0)
def PoB():
    global Deque
    if len(Deque) == 0:
        return -1
    else:
        return Deque.pop()
for i in range(int(input())):
    n = input()
    if n[:10] == "push_front":
        PuF()
    elif n[:9] == "push_back":
        PuB()
    elif n == "front":
        print(front())
    elif n == "back":
        print(back())
    elif n == "size":
        print(size())
    elif n == "empty":
        print(empty())
    elif n == "pop_front":
        print(PoF())
    elif n == "pop_back":
        print(PoB())