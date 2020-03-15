N,M = map(int,input().split())
order = []
for _ in range(N):
    s = input().split()
    if s[0] == "order":
        order.append([int(s[2]),int(s[1])])
    elif s[0] == "sort":
        order.sort()
    elif s[0] == "complete":
        for i,n in enumerate(order):
            if n[1] == int(s[1]):
                order.pop(i)
                break
    if len(order) == 0:
        print("sleep")
    else:
        for t,i in order:
            print(i,end=' ')
        print()
